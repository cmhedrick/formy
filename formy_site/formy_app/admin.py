from django.contrib import admin

from .models import Credential, Spreadsheet, SpreadsheetField

admin.site.register(Credential)
admin.site.register(Spreadsheet)
admin.site.register(SpreadsheetField)
