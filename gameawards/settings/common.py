import sys
from os.path import abspath, basename, dirname, join, normpath

from django.core.mail import send_mail

#Initialization of Are you human
import ayah
ayah.configure("15aaa63b65ead6b11342d1c7f349c68e875a3f16", "5d736518475d70a969d57bf2caadb32ce7160500")


########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory.
DJANGO_ROOT = dirname(dirname(abspath(__file__)))


# Site name.
SITE_NAME = basename(DJANGO_ROOT)

# Absolute filesystem path to the top-level project folder.
SITE_ROOT = dirname(DJANGO_ROOT)

# Add all necessary filesystem paths to our system path so that we can use
# python import statements.
sys.path.append(SITE_ROOT)
sys.path.append(normpath(join(DJANGO_ROOT, 'apps')))
sys.path.append(normpath(join(DJANGO_ROOT, 'libs')))




ADMINS = (
    ('admin', 'web@gameawards.com'),
)




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


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': SITE_ROOT+'/logs/mylog.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },  
        'request_handler': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': SITE_ROOT+'/logs/django_request.log',
                'maxBytes': 1024*1024*5, # 5 MB
                'backupCount': 5,
                'formatter':'standard',
        },
        'info': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': SITE_ROOT+'/logs/info.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        }, 
    },
    'loggers': {
        '': {
            'handlers': ['default', 'info'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'gameawards'
EMAIL_HOST_PASSWORD = 'greenballs'
DEFAULT_FROM_EMAIL = 'no-reply@gameawards.no'
SERVER_EMAIL = 'no-reply@gameawards.no'
