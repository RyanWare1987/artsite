# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from gallery.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        'user',
    ]


admin.site.register(Profile, ProfileAdmin)
