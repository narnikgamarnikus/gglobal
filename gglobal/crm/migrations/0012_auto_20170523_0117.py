# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 22:17
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20170523_0031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RemoveField(
            model_name='appeal',
            name='comment',
        ),
        migrations.AddField(
            model_name='activity',
            name='appeal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Appeal', verbose_name='Номер обращения'),
        ),
        migrations.AddField(
            model_name='appeal',
            name='activities',
            field=models.ManyToManyField(blank=True, related_name='_appeal_activities_+', to='crm.Activity', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='created_by',
            field=annoying.fields.AutoOneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='leed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Leed', verbose_name='Лид'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Project', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Source', verbose_name='Источник'),
        ),
        migrations.AlterField(
            model_name='project',
            name='activities',
            field=models.ManyToManyField(related_name='_project_activities_+', to='crm.Activity'),
        ),
    ]
