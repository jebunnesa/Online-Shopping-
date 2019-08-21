# Generated by Django 2.2.4 on 2019-08-20 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopping_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Mobile_no',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Invalid Mobile No.', regex='^(?:\\+?88)?01[1-9]\\d{8}$')]),
        ),
    ]