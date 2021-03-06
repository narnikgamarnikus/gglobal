# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-11 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0003_set_site_domain_and_name'),
        ('auth', '0008_alter_user_username_max_length'),
        ('crm', '0002_auto_20170611_2007'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.ManyToManyField(to='crm.PhoneNumber', verbose_name='Номера телефонов'),
        ),
        migrations.AddField(
            model_name='user',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', verbose_name='Сайты'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
