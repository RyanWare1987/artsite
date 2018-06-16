from base import *

# This is for Dev mode overwrites to the base.py settings file
DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#Stripe Environment Variables if any
STRIPE_PUBLISHABLE = os.environ.get('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.environ.get('STRIPE_SECRET')
