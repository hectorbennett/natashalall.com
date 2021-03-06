# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-29 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0033_auto_20180426_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='exhibitions',
            field=models.ManyToManyField(blank=True, help_text='Artworks can also be added to exhibitions from the exhibition edit screen.', to='exhibitions.Exhibition', verbose_name='exhibited in'),
        ),
    ]
