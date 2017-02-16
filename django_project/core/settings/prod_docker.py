
"""Configuration for production server"""
# noinspection PyUnresolvedReferences
from .prod import *  # noqa
import os
print os.environ

DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Muhammad Anis', 'anisiconic@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USERNAME'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': 5432,
        'TEST_NAME': 'unittests',
    }
}


# See fig.yml file for postfix container definition
#
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Host for sending e-mail.
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.csir.co.za')
# Port for sending e-mail.
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 25))
# SMTP authentication information for EMAIL_HOST.
# See fig.yml for where these are defined
#EMAIL_HOST_USER = 'user@do.ma.in'
#EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_FROM', 'no-reply@csir.co.za')
EMAIL_SUBJECT_PREFIX = '[Anis]'
