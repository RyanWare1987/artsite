# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180610_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='instagram_url',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
