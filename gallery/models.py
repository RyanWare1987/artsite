# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User



class Image(models.Model):
    # need to link author to the registered user in the table
    author = models.ForeignKey(User, related_name='blog_posts') #check related name
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tags = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True) # check upload dir

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Think about a image_height and image_width field on this model
# How can we have control when sizes of pictures could be Portrait or Landscape etc
# Perhaps incorporate a max_iamge_height etc?



class Profile(models.Model):
    # This model will hold the basic user information. The user's
    # profile will be customizable at some stage. This is not where
    # sensitive info such as email and password go.

    user = models.OneToOneField(User)
    # Here we create our custom fields that are available to each user in their profile
    name = models.CharField(max_length=80, default='')
    profile_pic = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True) # Model field reference
    date_of_birth = models.DateField(blank=True, null=True)
    website = models.URLField(max_length=100, default='')
    fav_artist = models.CharField(max_length=100, default='')
    medium = models.CharField(max_length=80, default='')
    occupation = models.CharField(max_length=50, default='')
    about_me = models.CharField(max_length=500, default='')
    facebook_url = models.URLField(max_length=100, default='')
    twitter_url = models.URLField(max_length=100, default='')
    instagram_url = models.URLField(max_length=100, default='')



    def __unicode__(self):
        return self.user.username