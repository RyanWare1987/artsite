# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import uuid
#import settings (path)?
from datetime import datetime
from django.contrib import admin
from django.core.files.base import ContentFile
from .forms import PortfolioForm, ImagePostForm
from .models import Image, Profile, Portfolio

#Make Portfolio
@admin.register(Portfolio)
class PortfolioModelAdmin(admin.ModelAdmin):
    form = PortfolioForm
    #prepopulated_fields = {'slug': ('title',)}
    fields = ('author', 'description', 'thumb', 'title', 'slug') #Moved title into pre-pop
    list_display = ('title', 'thumb') #Special field types in here (list change)
    list_filter = ('created_date',)

    def save_model(self ,request, obj, form, change):
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.modified = datetime.now()
            portfolio.save()

            super(PortfolioModelAdmin, self).save_model(request, obj, form, change)

# Need a way to upload single images?



# In case image should be removed from Album  ---  This was giving django.contrib.admin.sites.AlreadyRegistered: The model Image is already registered
#@admin.register(Image)
#class IImageModelAdmin(admin.ModelAdmin):
#    list_display = ('title', 'portfolio')
#    list_filter = ('portfolio', 'created_date')


#from reusable_blog admin
admin.site.register(Image)