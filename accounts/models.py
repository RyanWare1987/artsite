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
 



class Image(models.Model): # Do we need this to go away?
    description = models.CharField(max_length=300, default='')
    image = models.ImageField(upload_to='images/%Y/%m/%d/') # This path would go to S3 - check notepad++
    uploaded_at = models.DateTimeField(auto_now_add=True)
  
    

    