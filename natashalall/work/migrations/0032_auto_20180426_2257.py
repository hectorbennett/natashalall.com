# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-26 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import work.models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0031_auto_20180426_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkimage',
            name='image_original',
            field=models.ImageField(upload_to=work.models.image_filename, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='artworkvideo',
            name='url',
            field=models.CharField(help_text='At the moment this only supports youtube links', max_length=300),
        ),
    ]
