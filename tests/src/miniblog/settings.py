# Django settings for weblog project.
import os
import sys
ROOT=os.path.join(os.path.dirname(__file__), '../../')

# Add this package library directory
pack_dir = os.path.join(ROOT, '../')
pack_dir = os.path.realpath(pack_dir)
if pack_dir not in sys.path:
    sys.path.insert(0, pack_dir)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT, 'database.db'),
        'USER': '',                      
        'PASSWORD': '',                  
        'HOST': '',                      
        'PORT': '',                      
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(ROOT, 'static', 'collection')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4et6(22#@lgie4wogk)6um6^jklpkk0!z-l%uj&kvs*u2xrvfj%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    # This flavour loader is required to enable flavour template system.
    'mfw.template.loaders.flavour.Loader',

    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    # Adding these context processors are optional
    "mfw.context_processors.device",
    "mfw.context_processors.flavour",
)

MIDDLEWARE_CLASSES = (
    # This DeviceDetectionMiddleware must come first
    'mfw.middleware.device.DeviceDetectionMiddleware',

    # CacheBasedSessionMiddleware requires the following middlewares to enable
    # django's cache system.
    'django.middleware.cache.UpdateCacheMiddleware',            
    'django.middleware.common.CommonMiddleware',                
    'django.middleware.cache.FetchFromCacheMiddleware',         

    # This CacheBasedSessionMiddleware is required to enable session with the
    # device which does not support cookie. Comment out existing
    # SessionMiddleware
    'mfw.middleware.session.CacheBasedSessionMiddleware',       
    #'django.contrib.sessions.middleware.SessionMiddleware',

    # This SessionBasedCsrfViewMiddleware is required to enable csrf with the
    # device which does not support cookie. Comment out existing
    # CsrfViewMiddleware
    'mfw.middleware.csrf.SessionBasedCsrfViewMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',

    # This DeviceFlavourDetectionMiddleware is required to enable flavour
    # template system.
    'mfw.middleware.flavour.DeviceFlavourDetectionMiddleware',
                                                                
    # This DeviceEncodingMiddleware is required to convert response encoding
    #'mfw.middleware.encoding.DeviceEncodingMiddleware',
    'mfw.contrib.emoji.middleware.DeviceEmojiTranslationMiddleware',
                                                                                                                            
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'miniblog.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'miniblog.autocmds',
    'miniblog.blogs',
    'mfw',
    'mfw.contrib.emoji',
)

# Ingoring non relible mobile is not useful for debugging
MFW_DEVICE_IGNORE_NON_RELIBLE_MOBILE = not DEBUG

FIXTURE_DIRS = (
    os.path.join(ROOT, 'fixtures'),
)

LOGIN_REDIRECT_URL = '/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

try:
    from local_settings import *
except ImportError:
    pass