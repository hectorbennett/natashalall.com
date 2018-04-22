# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-22 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0023_artworkaudio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkaudio',
            name='artwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio', to='work.Artwork', verbose_name='audio clips'),
        ),
    ]
