# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-22 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0025_auto_20180422_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkaudio',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
