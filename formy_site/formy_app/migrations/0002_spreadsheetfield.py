# Generated by Django 3.0.6 on 2020-05-23 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formy_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=50)),
                ('field_type', models.CharField(choices=[('INTEGER', 'Integer/Number'), ('STRING', 'String/Text'), ('BOOL', 'True/False')], default='STRING', max_length=32)),
                ('spreadsheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formy_app.Spreadsheet')),
            ],
        ),
    ]
