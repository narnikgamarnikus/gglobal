# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-24 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        ('users', '0006_auto_20170424_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastercrmprofile',
            name='city',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
        ),
        migrations.AddField(
            model_name='mastercrmprofile',
            name='country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country'),
        ),
    ]