from base import *
import dj_database_url

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config('DATABASE_URL')   
}


#Stripe Environment Variables
STRIPE_PUBLISHABLE = os.environ.get('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.environ.get('STRIPE_SECRET')


SITE_URL = 'https://artsite-ryanware.herokuapp.com'
ALLOWED_HOSTS.append('artsite-ryanware.herokuapp.com')


# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
