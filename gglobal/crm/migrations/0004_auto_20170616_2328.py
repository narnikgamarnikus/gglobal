# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-16 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20170616_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelist',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executant_price', to='service.Service', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='trouble',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executant_price', to='service.Trouble', verbose_name='Проблема'),
        ),
    ]