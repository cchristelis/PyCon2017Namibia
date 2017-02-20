# coding=utf-8
"""Project level url handler."""
from django.contrib import admin
from django.conf.urls import url
from pycon.api_views.visitors import VisitorsApi
from pycon.views.visitor import VisitorCreate
from pycon.views.visitor import VisitorMapView

admin.autodiscover()
urlapi = [
    url(
        r'api/conference/(?P<conference_id>\d+)/visitors$',
        VisitorsApi.as_view())
]

urlpatterns = urlapi + [
    # TODO make landing page
    url(
        r'',
        view=VisitorMapView.as_view(),
        name='visitor-map'),
    url(
        r'map',
        view=VisitorMapView.as_view(),
        name='visitor-map'),
    url(
        r'visitor/add',
        VisitorCreate.as_view(success_url="/visitor/add"),
        name="visitor-add"),
]
