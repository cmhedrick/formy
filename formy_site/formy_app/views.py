import gspread
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# we want to allow
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

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
        except:
            return HttpResponse("Invalid header found.")
        return redirect("formy_app:success")
    return render(request, "form.html", {"form": form, "title": spreadsheet.title})


@xframe_options_exempt
def success_view(request):
    return render(request, "success.html")
