# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_images',
            field=models.ImageField(blank=True, height_field='image_height', upload_to='media', width_field='image_width'),
        ),
    ]
