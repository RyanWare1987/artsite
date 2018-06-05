# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView
from .models import Image, Profile, Portfolio
from .forms import ImagePostForm, ProfileEditForm


# The Gallery which contains the Images for each user
def gallery(request):
    #list = Portfolio.objects.filter(is_visible=True).order_by('-created')
    portfolios = Portfolio.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(portfolios, 6)

    page = request.GET.get('page')
    try: 
        portfolios = paginator.page('page')  #portfolios correctly referenced from models?
    except PageNotAnInteger:
        portfolios = paginator.page(1) #Loads first page if target is not an int
    except EmptyPage:
        portfolios = paginator.page(paginator.num_pages) #Loads last page if breached range

    return render(request, 'gallery.html', {'portfolios': portfolios}) # Will use the new gallery page

# List of images, orders by views or published date. Consider adding more filters, even 'likes'
def image_list(request):
    top = request.GET.get('top', False)
    if top:  #  Rbinz said ignore this error
        images = Image.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:3]
    else:
        images = Image.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "gallery/imagetests.html", {'images': images})


# Detail of the image, with own html page. Included a view counter
def image_detail(request, id):
    image = get_object_or_404(Image, pk=id)
    image.views +=1 # This counts the number of image views
    image.save()
    return render(request, "gallery/imagedetail.html", {'image': image})


# The new image view, which allows a user to upload a new image using the NewImageForm
def new_image(request):
    if request.method == "POST":
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            image.published_date = timezone.now()
            image.save()
            return redirect(image_detail, image.pk)
    else: 
        form = ImagePostForm()
    return render(request, 'gallery/imagepostform.html', {'form': form})



@login_required(login_url='/login/')
def edit_profile(request):
    # This looks for the current user's Profile model and sets it to user_profile
    try: 
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        user_profile = None
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        pe_form = ProfileEditForm(request.POST, instance=user_profile)

        if pe_form.is_valid():
            # We do not want to commit the save right away. 
            # Instead we match the user_id of the user to the profile.
            profile = pe_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile page updated successfully!")
            return redirect('profile')
        else: 
            messages.error(request, "Oops, there was an error - Please try again")
    else:
        pe_form = ProfileEditForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'PEform': pe_form})


def handler404(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'error404.html', None, None, 404)

