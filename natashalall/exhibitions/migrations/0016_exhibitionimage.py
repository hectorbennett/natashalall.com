# Generated by Django 2.0.4 on 2018-04-29 17:13

from django.db import migrations, models
import django.db.models.deletion
import exhibitions.models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitions', '0015_auto_20180426_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_original', models.ImageField(upload_to=exhibitions.models.image_filename, verbose_name='exhibition')),
                ('visible', models.BooleanField(default=True)),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibitions', to='exhibitions.Exhibition')),
            ],
        ),
    ]
