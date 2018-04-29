from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm, UserEditForm, ProfileEditForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import User, Profile
import json



#Ensure this register cuts out all payment options for now
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
 
            user = auth.authenticate(username=request.POST.get('username'),
                                     email=request.POST.get('email'),
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


@login_required(login_url='/login/')
def edit_profile(request):
    # This looks for the current user's Profile model and sets it to user_profile
    try: 
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        user_profile = None

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