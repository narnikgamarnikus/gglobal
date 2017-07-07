# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 13:27
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20170706_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '600x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
