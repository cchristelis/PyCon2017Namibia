__author__ = 'Christian Christelis <christian@kartoza.com>'

from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    GeometrySerializerMethodField)
from pycon.models.visit import Visit
from rest_framework.views import APIView
from rest_framework.response import Response


class AttendeeGeoSerializer(GeoFeatureModelSerializer):
    geometry = GeometrySerializerMethodField()

    def get_geometry(self, obj):
        return None

    class Meta:
        model = Visit
        geo_field = 'home'
        exclude = []

    def to_representation(self, instance):
        result = super(AttendeeGeoSerializer, self).to_representation(instance)
        result['properties']['id'] = instance.id
        return result


class ListAttendees(APIView):

    def get(self, request, format=None):
        visit_set = Visit.objects.all()
        serializers = self.serialize(visit_set)
        return Response(serializers.data)

    def serialize(self, set):
        return AttendeeGeoSerializer(set, many=True)
