# Generated by Django 3.1.7 on 2021-04-19 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_motoreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motoreview',
            name='moto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='homepage.moto'),
        ),
    ]
