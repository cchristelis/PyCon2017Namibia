# coding=utf-8
"""
core.settings.contrib
"""
from .base import *  # noqa

# Extra installed apps
INSTALLED_APPS += (
    'rest_framework',
    'rest_framework_gis',
    'django_countries',
    'pycon',
)
