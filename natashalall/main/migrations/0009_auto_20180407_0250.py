# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-07 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_shows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedialinks',
            name='name',
            field=models.CharField(blank=True, choices=[('FB', 'Facebook'), ('SC', 'Soundcloud'), ('OT', 'OT')], default='OT', max_length=2, null=True),
        ),
    ]
