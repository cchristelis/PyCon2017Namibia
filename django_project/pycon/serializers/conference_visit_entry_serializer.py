__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '16/02/17'

from rest_framework import serializers
from pycon.models.conference_visit_entry import ConferenceVisitEntry
from pycon.serializers.conference_serializer import ConferenceSerializer
from pycon.serializers.visit_serializer import VisitSerializer


class ConferenceVisitEntrySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('is_named_bar')

    def is_named_bar(self, instance):
        return instance.__unicode__()

    class Meta:
        model = ConferenceVisitEntry
        fields = '__all__'

    def to_representation(self, instance):
        result = super(ConferenceVisitEntrySerializer, self).to_representation(instance)
        result['conference'] = ConferenceSerializer(instance.conference).data
        result['visit'] = VisitSerializer(instance.visit).data
        return result
