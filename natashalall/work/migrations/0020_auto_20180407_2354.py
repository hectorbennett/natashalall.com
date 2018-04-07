# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-07 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0019_auto_20180407_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='creation_date',
            field=models.DateField(help_text='You can just put 01/01/yyyy if you only know the year.'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='exhibitions',
            field=models.ManyToManyField(blank=True, help_text='Artworks can also be added to exhibitions from the exhibitionedit screen.', to='exhibitions.Exhibition', verbose_name='exhibited in'),
        ),
        migrations.AlterField(
            model_name='artworkvideo',
            name='url',
            field=models.CharField(help_text='Must be in the format https://www.youtube.com/embed/x-xxxxxxxxx', max_length=300),
        ),
    ]
