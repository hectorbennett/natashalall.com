# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-07 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0016_auto_20180407_0605'),
        ('exhibitions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='artworks',
            field=models.ManyToManyField(to='work.Artwork'),
        ),
    ]
