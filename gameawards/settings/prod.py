from gameawards.settings.common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gameawards',    # Or path to database file if using sqlite3.
        'USER': 'gameawards',                      # Not used with sqlite3.
        'PASSWORD': 'greenballs',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = '/home/gameawards/webapps/gamedia/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = '/home/gameawards/webapps/gastatic/'
STATICFILES_DIRS = (DJANGO_ROOT+"/static",)
TEMPLATE_DIRS = (DJANGO_ROOT+'/templates')

