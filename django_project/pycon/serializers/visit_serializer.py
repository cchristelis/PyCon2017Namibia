__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '16/02/17'

import hashlib
from rest_framework import serializers
from pycon.models.visit import Visit


class VisitSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('is_named_bar')
    gravatar_url = serializers.SerializerMethodField()
    conference_name = serializers.SerializerMethodField()

    def is_named_bar(self, instance):
        return instance.__unicode__()

    class Meta:
        model = Visit
        fields = '__all__'

    def get_gravatar_url(self, obj):
        email = obj.gravatar
        size = 40

        # construct the url
        gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()

        return gravatar_url

    def get_conference_name(self,obj):
        conference = obj.conference
        return "[%s]%s" % (conference.conference_name,conference.conference_code)
