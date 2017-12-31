# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_shows_socialmedialinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtworkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_original', models.ImageField(upload_to=main.models.image_filename)),
            ],
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='image_original',
        ),
        migrations.AddField(
            model_name='artworkimage',
            name='artwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.Artwork'),
        ),
    ]