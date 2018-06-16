from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm
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



def register(request):
    """
    This view handles the register request, and 
    calls forth the UserRegistrationForm
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
 
            user = auth.authenticate(email=request.POST.get('email'), 
                                     password=request.POST.get('password1'))
            """
            We are authenticating against a user's
            email entered and password. Scope to add 
            authentication against a username also here
            """
                                     
                                     
 
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('edit_profile'))
                """
                If everything went smoothly, the user
                is redirected to a page to edit their profile, which is 
                created and assigned to their user.
                """
 
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
    """
    We want the profile view only available to those
    who have logged in, as the profile view won't know
    who's information to pull forward otherwise
    """
    return render(request, 'profile.html')



def login(request):
    """
    Handle's a user login. We run authentication
    against a user's email and password.
    """
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
                """
                If authentication fails for whatever reason, we don't
                specify into the details, just display this error
                """
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    """
    Logout request, currently this is only
    displayed to user's who are logged in within
    the base.html page so no need to have
    @login_required prefixing this
    """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return render(request, 'index.html')
