# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid  #only needed for 'slug' 
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    # This model will hold the basic user information. The user's
    # profile will be customizable at some stage. This is not where
    # sensitive info such as email and password go.

    user = models.OneToOneField(User)
    # Here we create our custom fields that are available to each user in their profile
    name = models.CharField(max_length=80, default='')
    date_of_birth = models.DateField(blank=True, null=True)
    website = models.URLField(max_length=100, blank=True)
    fav_artist = models.CharField(max_length=100, blank=True)
    medium = models.CharField(max_length=80, blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    about_me = models.CharField(max_length=500, blank=True)
    facebook_url = models.URLField(max_length=100, blank=True)
    twitter_url = models.URLField(max_length=100, blank=True)
    instagram_url = models.URLField(max_length=100, blank=True)
    linkedin_url = models.URLField(max_length=100, blank=True)
    youtube_url = models.URLField(max_length=90, blank=True)
    pintrest_url = models.URLField(max_length=90, blank=True)


    def __unicode__(self):
        return self.user.username