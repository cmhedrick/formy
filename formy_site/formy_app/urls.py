from django.contrib import admin
from django.urls import path

from . import views

app_name = "formy_app"

urlpatterns = [
    path("form/<int:spreadsheet_id>", views.custom_form_view, name="contact"),
    path("success/", views.success_view, name="success"),
]
