# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-25 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_siteconfig_copyright_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfig',
            name='copyright_line',
            field=models.CharField(default='Copyright', help_text="The copyright text that appears in the footer.E.g. 'Copyright the artist'", max_length=255),
        ),
    ]
