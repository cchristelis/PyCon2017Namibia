# coding=utf-8
"""
core.settings.contrib
"""
from .base import *  # noqa
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
# Extra installed apps
INSTALLED_APPS += (
    'rest_framework',
    'rest_framework_gis',
    'django_countries',
)
