# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-06 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_auto_20170506_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autocreateclientprocess',
            name='service',
            field=models.ManyToManyField(blank=True, to='service.Service'),
        ),
        migrations.AlterField(
            model_name='autocreateclientprocess',
            name='trouble',
            field=models.ManyToManyField(blank=True, to='service.Trouble'),
        ),
    ]
