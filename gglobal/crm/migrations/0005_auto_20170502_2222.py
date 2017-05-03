# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-02 19:22
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20170502_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcrmprofile',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='clientcrmprofile',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='clientcrmprofile',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', verbose_name='Сайты'),
        ),
        migrations.AlterField(
            model_name='clientcrmprofile',
            name='user',
            field=annoying.fields.AutoOneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
    ]