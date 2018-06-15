"""
Django settings for artsite project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Url will go into this box below
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0', 'artsite-ryanware.herokuapp.com']

SITE_ID = 1

LOGIN_URL = '/login/'

# Set the User Model and backend authenticator
# Removed AUTH_USER_MODEL = 'accounts.User'  -  As this conflicts with the model [class 'Profile']

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'accounts.backends.EmailAuth',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_forms_bootstrap',
    'rest_framework',
    'tinymce',
    'emoticons',
    'disqus',
    'home',
    'accounts',
    'artwork',
    'gallery',
    'imagekit',
    'material',
    'basket',
    'material.admin',
    'easy_thumbnails',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'artsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'artsite.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", "js", "tinymce", "tinymce.min.js")


SITE_URL = 'http://127.0.0.1:8000'
ALLOWED_HOSTS.append(u'0.0.0.0',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'testing@example.com'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'removed'
EMAIL_HOST_PASSWORD = 'removed'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#Sendgrid needs testing once deployed that emails actually land where they are pointed to


#Amazon AWS Settings
AWS_STORAGE_BUCKET_NAME = 'artsite-ryanware-s3bucketstorage'
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

#Tell django-storages the domain and use to refer to static files
AWS_S3_CUSTOM_DOMAIN = 's3.eu-west-2.amazonaws.com/artsite-ryanware-s3bucketstorage'


#SITE_URL = os.environ['ARTSITE_SITE_URL']
#ALLOWED_HOSTS.append(os.environ['ARTSITE_ALLOWED_HOST'])

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
STATIC_URL = 'https://s3.eu-west-2.amazonaws.com/artsite-ryanware-s3bucketstorage/'
MEDIA_URL = 'https://s3.eu-west-2.amazonaws.com/artsite-ryanware-s3bucketstorage/'
#STATIC_URL = '/static/'
#STATIC_ROOT = 'static'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#MEDIA_URL = STATIC_URL + 'media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#STATICFILES_DIRS = (
        #os.path.join(BASE_DIR, "static"),
        #)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
