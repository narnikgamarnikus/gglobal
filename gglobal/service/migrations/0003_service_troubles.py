# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-17 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20170615_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='troubles',
            field=models.ManyToManyField(to='service.Trouble'),
        ),
    ]
