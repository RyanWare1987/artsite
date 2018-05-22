from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm, UserEditForm, ImageForm
from django.core.urlresolvers import reverse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import User
from gallery.models import Profile
import json



#Ensure this register cuts out all payment options for now
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
 
            user = auth.authenticate(email=request.POST.get('email'),  #Find a way for it to check against both values
                                     password=request.POST.get('password1'))
                                     
                                     
 
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('edit_profile'))
 
            else:
                messages.error(request, "unable to log you in at this time!")
        else: 
            messages.error(request, "Error something was entered incorrectly")
 
    else:
        form = UserRegistrationForm()
 
    args = {"active": "register", "form": form}
    args.update(csrf(request))
 
    return render(request, 'register.html', args)



@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return render(request, 'index.html')




 ##Better Image Upload View  - wont work as profile has moved apps
def image_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'image_form_upload.html', {
        'form': form
    })