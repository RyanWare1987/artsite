# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-17 20:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('tags', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('website', models.URLField(default='', max_length=100)),
                ('fav_artist', models.CharField(default='', max_length=100)),
                ('medium', models.CharField(default='', max_length=80)),
                ('occupation', models.CharField(default='', max_length=50)),
                ('about_me', models.CharField(default='', max_length=500)),
                ('facebook_url', models.URLField(default='', max_length=100)),
                ('twitter_url', models.URLField(default='', max_length=100)),
                ('instagram_url', models.URLField(default='', max_length=100)),
                ('profile_pic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]