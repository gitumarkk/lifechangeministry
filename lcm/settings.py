"""
Django settings for lcm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l@bs#++l_13!-+j+5v1uvrk843u*#@jx-+n@ym6d4co6)z7k3+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party
    'south',  # data migration
    'django_nose',  # unittesting

    # Project
    'lcm.apps.frontpages',
    'lcm.apps.backend',
    'tinymce',
    'sorl.thumbnail',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# ========================================================
# TEMPLATES CONFIGURATION
# ========================================================
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "lcm.context_processors.highlight_active_menu")

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "lcm", "templates"),
)

# END OF TEMPLATES CONFIGURATION
# ========================================================

ROOT_URLCONF = 'lcm.urls'

WSGI_APPLICATION = 'lcm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lcm',
        'USER': 'postgres'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# ========================================================
# STATIC FILES CONFIGURATION
# ========================================================

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "lcm", "static"),
)

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# END OF STATIC FILES CONFIGURATION
# ========================================================


MEDIA_URL = '/media/'

MEDIA_ROOT =  os.path.join(BASE_DIR, "lcm", "media")

# ========================================================
# TEST RUNNER CONFIGURATION
# ========================================================
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


# ========================================================
# SOUTH TEST CONFIGURATIONS
# ========================================================
SKIP_SOUTH_TESTS = True     # Do not run the south tests as part of our
                            # test suite.
SOUTH_TESTS_MIGRATE = False  # Do not run the migrations for our tests.
                             # We are assuming that our models.py are correct
                             # for the tests and as such nothing needs to be
                             # migrated.


# ========================================================
# EMAILS
# ========================================================
MANDRILL_KEY = ''
TO_EMAIL = "gitumarkk+test@gmail.com"


# ========================================================
# CACHE
# ========================================================
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': "lcm",
    }
}

THUMBNAIL_DEBUG = DEBUG

# ========================================================
# HEROKU CONFIGURATIONS
# ========================================================
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Import production settings
try:
    from production_settings import *
except ImportError:
    pass
