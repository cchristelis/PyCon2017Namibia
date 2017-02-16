# coding=utf-8
"""Project level url handler."""
from django.contrib import admin
from django.conf.urls import url
from pycon.views.visitor import VisitorMapView

admin.autodiscover()
from django.conf.urls import url
from pycon.api_views.visitors import VisitorsApi
from pycon.views.visitor import VisitorCreate

urlapi = [
    url(
        r'api/conference/(?P<conference_id>\d+)/visitors$',
        VisitorsApi.as_view())
]

urlpatterns = urlapi + [
    url(r'map',
        view=VisitorMapView.as_view(),
        name='visitor-map'),
    url(r'visitor/add',VisitorCreate.as_view(), name="visitor-add"),
]
