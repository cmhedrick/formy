from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class UserProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Profile {self.user.username}"


class Credential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to="creds/%Y/%m/%d/")

    def __str__(self):
        return f"CRED: {self.user.email}"


class Spreadsheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.email}: {self.title}"


class SpreadsheetField(models.Model):
    INTEGER = "INTEGER"
    STRING = "STRING"
    BOOL = "BOOL"
    FIELD_CHOICES = [
        (INTEGER, "Integer/Number"),
        (STRING, "String/Text"),
        (BOOL, "True/False"),
    ]
    spreadsheet = models.ForeignKey(Spreadsheet, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=50)
    field_type = models.CharField(max_length=32, choices=FIELD_CHOICES, default=STRING,)

    def __str__(self):
        return f"SpreadID:{self.spreadsheet.title}| {self.spreadsheet.title}: {self.field_name}"
