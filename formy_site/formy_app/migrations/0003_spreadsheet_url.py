# Generated by Django 3.0.6 on 2020-05-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formy_app', '0002_spreadsheetfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='spreadsheet',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
