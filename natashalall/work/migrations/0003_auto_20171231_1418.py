# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-31 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_artworkvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='artworkimage',
            name='hidden',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='artworkimage',
            name='thumbnail',
            field=models.BooleanField(default=0),
        ),
    ]
