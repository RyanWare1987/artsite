# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-13 07:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20180612_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='stripe_id',
        ),
    ]
