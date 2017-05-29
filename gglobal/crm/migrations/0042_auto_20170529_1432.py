# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 11:32
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0041_auto_20170528_2222'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='clientprofile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='project',
            name='address',
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='user',
            field=annoying.fields.AutoOneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='owner',
            field=annoying.fields.AutoOneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Мастер'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Project', verbose_name='Заказ'),
        ),
    ]
