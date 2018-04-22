# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-22 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0027_artwork_live'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkaudio',
            name='url',
            field=models.CharField(help_text="Must be in the format '<iframe>...</iframe>'. You can find the code for this in the embed section of the share dialog in soundcloud.", max_length=500),
        ),
    ]