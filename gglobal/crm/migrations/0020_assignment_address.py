# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_auto_20170526_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Address'),
        ),
    ]
