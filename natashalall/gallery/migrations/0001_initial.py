# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='artwork/%Y/%m/')),
                ('title', models.CharField(max_length=200)),
                ('medium', models.CharField(max_length=200)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('description', models.TextField()),
                ('date_created', models.DateField()),
                ('date_published', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
