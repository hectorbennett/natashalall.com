# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import work.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('creation_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ArtworkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_original', models.ImageField(upload_to=work.models.image_filename)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='work.Artwork')),
            ],
        ),
    ]