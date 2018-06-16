# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid 
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    This model will contain all of the user's information that is 
    intended to be publically viewable. No sensitive information
    should be stored here, as the plan going forward is to have this
    viewable by other users.
    - name is the only model we require, the rest are optional
    - We link the Profile model to the User model in a OneToOneField
    - URLFields are used for inputs that are URL's
    - CharFields the standard input for regular data fields
    - DateField used for the user's date of birth
    """

    user = models.OneToOneField(User)
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