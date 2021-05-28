# Generated by Django 3.1.7 on 2021-05-28 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='accepted_terms',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='licence_cat',
            field=models.CharField(blank=True, choices=[('AM', 'AM'), ('A1', 'A1'), ('A2', 'A2'), ('A', 'A')], default='A', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='licence_valid_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
