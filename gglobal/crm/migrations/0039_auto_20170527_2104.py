# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 18:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0038_appeal_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='master',
            new_name='owner',
        ),
    ]
