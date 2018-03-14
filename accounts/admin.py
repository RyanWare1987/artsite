# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    # This will display a list of users in the admin panel

    list_display = [
        'user',
    ]


admin.site.register(Profile, ProfileAdmin)