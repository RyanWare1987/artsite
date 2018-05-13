# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Image
from .forms import ImagePostForm
from django.shortcuts import redirect


# List of images, orders by views or published date. Consider adding more filters, even 'likes'
def image_list(request):
    top = request.GET.get('top', False)
    if top:  #  Don't know why this is failing wih E1101 Class Image has no objects member
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

