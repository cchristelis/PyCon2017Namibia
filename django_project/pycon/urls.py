# coding=utf-8
"""Project level url handler."""
from django.contrib import admin
from django.conf.urls import url
from pycon.views.visitor import VisitorMapView

admin.autodiscover()
from django.conf.urls import url
from pycon.api_views.visitors import VisitorsApi

urlpatterns =[
    url(regex='',
        view=VisitorMapView.as_view(),
        name='visitor-map'),
    url(
        r'^api/visitors/(?P<conference_id>\d+)$',
        VisitorsApi.as_view()),
]
