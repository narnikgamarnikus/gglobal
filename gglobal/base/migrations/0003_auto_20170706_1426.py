# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_image_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='alt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]