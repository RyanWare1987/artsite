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