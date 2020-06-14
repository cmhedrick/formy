import datetime

import gspread
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# we want to allow iframes to send data
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .forms import CustomForm
from .models import User, Spreadsheet, SpreadsheetField, Credential
from .spreadsheet_utils import next_available_row


@csrf_exempt
@xframe_options_exempt
def custom_form_view(request, spreadsheet_id=None):
    spreadsheet = Spreadsheet.objects.get(id=spreadsheet_id)

    if request.method == "GET":
        form = CustomForm(context=request, spreadsheet=spreadsheet)

    else:
        cred = Credential.objects.get(user=spreadsheet.user)
        gs_client = gspread.service_account(filename=cred.file.path)
        google_spreadsheet = gs_client.open_by_url(spreadsheet.url)
        worksheet = google_spreadsheet.sheet1
        row = next_available_row(worksheet)
        try:
            for index, field in enumerate(request.POST):
                if index == 0:
                    index += 1
                if not field == "csrfmiddlewaretoken":
                    worksheet.update_cell(row, index, request.POST[field])
            if spreadsheet.track_sub_times:
                index += 1
                worksheet.update_cell(
                    row, index, timezone.now().strftime("%d/%m/%Y %H:%m")
                )

        except:
            return HttpResponse("Invalid header found.")
        form = CustomForm(context=request, spreadsheet=spreadsheet)
        return render(
            request,
            "form.html",
            {
                "form": form,
                "title": spreadsheet.title,
                "success_msg": "Success! Thanks for submitting!",
            },
        )
    return render(request, "form.html", {"form": form, "title": spreadsheet.title})


@xframe_options_exempt
def success_view(request):
    return render(request, "success.html")
