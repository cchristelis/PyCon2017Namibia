# coding=utf-8
"""Project level url handler."""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns=[
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('pycon.urls', namespace='pycon')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
