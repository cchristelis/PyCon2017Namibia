# coding=utf-8
"""Project level url handler."""
from django.conf.urls import patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
)
