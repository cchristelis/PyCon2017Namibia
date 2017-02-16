__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '16/02/17'

from rest_framework import serializers
from pycon.models.conference import Conference


class ConferenceSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('is_named_bar')

    def is_named_bar(self, instance):
        return instance.__unicode__()

    class Meta:
        model = Conference
        fields = '__all__'
