from .base import *
from .security import *

ALLOWED_HOSTS = ['staging.{{ project_name }}', ]

DEBUG = True
TEMPLATE_DEBUG = DEBUG
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}',
        # The following settings are not used with sqlite3:
        'USER': '{{ project_name }}',
        'PASSWORD': '{{ project_name }}',
        'HOST': '127.0.0.1',             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
