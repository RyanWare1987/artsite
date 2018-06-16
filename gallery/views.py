# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView
from .models import Profile
from .forms import ProfileEditForm
import datetime


"""
We only want the option of editing
a profile available to someone
who is currently logged in
"""
@login_required(login_url='/login/')
def edit_profile(request):
    """
    We request the current user's profile to be edited.
    But will not proceed if the user has no profile.
    This however, should be impossible.
    """
    
    try: 
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        user_profile = None
    if request.method == 'POST':
        pe_form = ProfileEditForm(request.POST, instance=user_profile)

        if pe_form.is_valid():
            """
            We do not want to commit the save right away. 
            Instead we match the user_id of the user to the profile.
            """
            profile = pe_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile page updated successfully!")
            return redirect('profile')
        else: 
            messages.error(request, "There was an error - Please review and try again")
    else:
        pe_form = ProfileEditForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'PEform': pe_form})

