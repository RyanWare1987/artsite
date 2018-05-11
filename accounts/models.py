from __future__ import unicode_literals
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.utils import timezone
from django.conf import settings


class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
       Creates and saves a User with the given username, email and password.
       """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')
 
        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
 
        return user
 
class Profile(models.Model):
    # This model will hold the basic user information. The user's
    # profile will be customizable at some stage. This is not where
    # sensitive info such as email and password go.

    user = models.OneToOneField(User)
    # Here we create our custom fields that are available to each user in their profile
    name = models.CharField(max_length=80, default='')
    profile_pic = models.ImageField
    date_of_birth = models.DateField(blank=True, null=True)
    website = models.URLField(max_length=100, default='')
    fav_artist = models.CharField(max_length=100, default='')
    medium = models.CharField(max_length=80, default='')
    occupation = models.CharField(max_length=50, default='')
    about_me = models.CharField(max_length=500, default='')
    facebook_url = models.URLField(max_length=100, default='')
    twitter_url = models.URLField(max_length=100, default='')
    instagram_url = models.URLField(max_length=100, default='')


    def __unicode__(self):
        return self.user.username


class Image(models.Model):
    description = models.CharField(max_length=300, default='')
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
  
    

    