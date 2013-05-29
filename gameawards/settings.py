# Django settings for gameawards project.

import os, socket, ayah
from django.core.mail import send_mail

#Initialization of Are you human
ayah.configure("15aaa63b65ead6b11342d1c7f349c68e875a3f16","5d736518475d70a969d57bf2caadb32ce7160500")

#DEV SETTINGS
if socket.gethostname() == ("TheMatrix" or "Virus" or "xishan"):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    ADMINS = (
        ('admin', 'web@gameawards.com'),
    )

    MANAGERS = ADMINS

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '/home/jorgen/progging/gameawards/ngadb.db',    # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
    
    MEDIA_ROOT = '/home/jorgen/gameawards/media/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = '/home/jorgen/gameawards/static/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = ("/home/jorgen/progging/gameawards/static",)
    TEMPLATE_DIRS = ('/home/jorgen/progging/gameawards/templates')



# PRODUCTION SETTINGS
else:
    
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    ADMINS = (
        ('admin', 'web@gameawards.com'),
    )

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
    STATICFILES_DIRS = ("/home/gameawards/webapps/django/gameawards/static",)
    TEMPLATE_DIRS = ('/home/gameawards/webapps/django/gameawards/templates')


#COMMON SETTINGS
if True:

    TIME_ZONE = 'Europe/Oslo'

    LANGUAGE_CODE = 'en-us'

    SITE_ID = 1

    AUTH_PROFILE_MODULE = 'members.UserProfile'

    # The page users are directed to if they are not logged in when 
    # accessing a page that requires login.
    LOGIN_URL = ''

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True 
    
    
    ACCEPTED_UPLOAD_FILETYPES = ["pdf", "zip", "rar"]
    
    """
    2.5MB - 2621440
    5MB - 5242880
    10MB - 10485760
    20MB - 20971520
    50MB - 5242880
    100MB 104857600
    250MB - 214958080
    500MB - 429916160
    """
    MAX_UPLOAD_SIZE = 104857600
    
    FILE_UPLOAD_MAX_MEMORY_SIZE = 114857600

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = 'c^nyv!ky47%o+s46dzplm0)nfvt+k!@5j06l0at+$z2)-=ahr^'

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
        
    ROOT_URLCONF = 'gameawards.urls'

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = 'gameawards.wsgi.application'

    ACCOUNT_ACTIVATION_DAYS = 7

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        #'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django.contrib.admindocs',
        'news',
        'runs',
        'members',
        'content',
        'south',
        'gallery',
        
        
    )
    
    INTERNAL_IPS = ('127.0.0.1',)
    
    TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    )

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

    EMAIL_HOST = 'smtp.webfaction.com'
    EMAIL_HOST_USER = 'gameawards'
    EMAIL_HOST_PASSWORD = 'greenballs'
    DEFAULT_FROM_EMAIL = 'web@gameawards.no'
    SERVER_EMAIL = 'web@gameawards.no'
    




