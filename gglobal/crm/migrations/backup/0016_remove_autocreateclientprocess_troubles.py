# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-06 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0015_auto_20170506_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autocreateclientprocess',
            name='troubles',
        ),
    ]
