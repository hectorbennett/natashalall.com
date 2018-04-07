# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-06 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0011_artwork_exhibitions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkvideo',
            name='url',
            field=models.CharField(help_text='Must be in the format https://www.youtube.com/embed/x-xxxxxxxxx', max_length=300),
        ),
    ]
