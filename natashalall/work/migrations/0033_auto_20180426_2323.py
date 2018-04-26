# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-26 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0032_auto_20180426_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkaudio',
            name='url',
            field=models.CharField(help_text='Must be in iframe format. You can find the code for this in the embed section of the share dialog in soundcloud.', max_length=500, verbose_name='soundcloud url'),
        ),
        migrations.AlterField(
            model_name='artworkvideo',
            name='url',
            field=models.CharField(help_text='At the moment this only supports youtube links', max_length=300, verbose_name='youtube url'),
        ),
    ]
