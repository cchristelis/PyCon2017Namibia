__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '16/02/17'

from rest_framework import serializers
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer, GeometrySerializerMethodField)
from pycon.models.conference import Conference


class ConferenceSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('is_named_bar')

    def is_named_bar(self, instance):
        return instance.__unicode__()

    class Meta:
        model = Conference
        fields = '__all__'


class ConferenceGeoSerializer(GeoFeatureModelSerializer):
    name = serializers.SerializerMethodField('is_named_bar')

    def is_named_bar(self, available_layer):
        return available_layer.__unicode__()

    geometry = GeometrySerializerMethodField()

    def get_geometry(self, obj):
        return None

    class Meta:
        model = Conference
        geo_field = 'location'
        exclude = []

    def to_representation(self, instance):
        result = super(ConferenceGeoSerializer, self).to_representation(instance)
        return result
