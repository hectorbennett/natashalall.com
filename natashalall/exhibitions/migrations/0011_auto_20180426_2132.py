# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-26 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitions', '0010_auto_20180426_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
