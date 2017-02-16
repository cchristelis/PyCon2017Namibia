# coding=utf-8
"""Project level url handler."""
from django.contrib import admin
from django.conf.urls import url
from pycon.views.visitor import VisitorMapView

admin.autodiscover()
from django.conf.urls import url
from pycon.api_views.visitors import VisitorsApi

urlapi = [
    url(
        r'api/conference/(?P<conference_id>\d+)/visitors$',
        VisitorsApi.as_view())
]

urlpatterns = urlapi + [
    url(r'',
        view=VisitorMapView.as_view(),
        name='visitor-map'),
]
