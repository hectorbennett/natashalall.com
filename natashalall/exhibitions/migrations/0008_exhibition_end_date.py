# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-26 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitions', '0007_auto_20180426_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
