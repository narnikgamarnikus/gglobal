# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-04 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20170504_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True, verbose_name='Название')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Способ оплаты',
                'verbose_name_plural': 'Способы оплаты',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True, verbose_name='Название')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Описание')),
                ('bill_of_payer', models.CharField(max_length=255, null=True, verbose_name='Счёт получателя')),
                ('beneficiarys_account', models.CharField(max_length=255, null=True, verbose_name='Счёт плательщика')),
                ('cvv', models.CharField(max_length=3, null=True, verbose_name='CVV')),
            ],
            options={
                'verbose_name': 'Тип оплаты',
                'verbose_name_plural': 'Способы оплаты',
            },
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Пометка', 'verbose_name_plural': 'Пометки'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name': 'Счёт', 'verbose_name_plural': 'Счеты'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='payment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.PaymentType', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_method',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crm.PaymentMethod'),
            preserve_default=False,
        ),
    ]