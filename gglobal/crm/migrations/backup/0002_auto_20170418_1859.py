# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mastercrmprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='mastercrmprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='mastercrmprofile',
            name='sites',
        ),
        migrations.RemoveField(
            model_name='mastercrmprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='MasterCRMProfile',
        ),
    ]