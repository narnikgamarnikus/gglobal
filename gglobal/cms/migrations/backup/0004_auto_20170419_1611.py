# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-19 13:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.CITIES_CITY_MODEL),
        ('cms', '0003_surveypage_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveypage',
            name='city',
        ),
        migrations.AddField(
            model_name='homepage',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.CITIES_CITY_MODEL),
        ),
    ]
