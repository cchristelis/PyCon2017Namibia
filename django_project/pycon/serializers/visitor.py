from rest_framework import serializers
from rest_framework_gis.serializers import GeometrySerializerMethodField
# import code for encoding urls and generating md5 hashes
import urllib, hashlib

from django.core.exceptions import ObjectDoesNotExist
from pycon.models.visit import Visit

__author__ = 'Dimas Ciputra <dimas@kartoza.com>'
__date__ = '16/02/17'


class VisitorSerializer(serializers.ModelSerializer):

    gravatar_url = serializers.SerializerMethodField()

    class Meta:
        model = Visit
        fields = ('name', 'home', 'gravatar_url')

    def get_gravatar_url(self, obj):
        email = obj.gravatar
        size = 40

        # construct the url
        gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()

        return gravatar_url
