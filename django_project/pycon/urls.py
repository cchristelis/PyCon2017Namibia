# coding=utf-8
"""Project level url handler."""
from django.contrib import admin
from django.conf.urls import url
from pycon.views.visitor import VisitorMapView

admin.autodiscover()

urlpatterns =[
    url(regex='',
        view=VisitorMapView.as_view(),
        name='visitor-map'),
]
