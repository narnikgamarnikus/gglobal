# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_auto_20170526_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Address'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.ClientProfile', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='service',
            field=models.ManyToManyField(blank=True, to='service.Service', verbose_name='Услуги'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='trouble',
            field=models.ManyToManyField(blank=True, to='service.Trouble', verbose_name='Проблемы'),
        ),
        migrations.AlterField(
            model_name='leed',
            name='service',
            field=models.ManyToManyField(blank=True, to='service.Service', verbose_name='Услуги'),
        ),
        migrations.AlterField(
            model_name='leed',
            name='trouble',
            field=models.ManyToManyField(blank=True, to='service.Trouble', verbose_name='Проблемы'),
        ),
    ]
