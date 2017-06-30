# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 00:09
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20170617_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='state',
            field=django_fsm.FSMField(choices=[('new', 'Новая'), ('approved', 'Принял'), ('handed', 'Передана в работу')], default='new', max_length=50, protected=True, verbose_name='Статус'),
        ),
    ]
