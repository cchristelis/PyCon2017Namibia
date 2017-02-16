__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '16/02/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

import os
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from pycon.models.conference_visit_entry import ConferenceVisitEntry
from pycon.serializers.conference_visit_entry_serializer import ConferenceVisitEntrySerializer


class VisitorsApi(APIView):
    def get(self, request, conference_id=None):
        if conference_id:
            entry = ConferenceVisitEntry.objects.filter(conference=conference_id)
            serializer = ConferenceVisitEntrySerializer(entry, many=True)
            return Response(serializer.data)
        else:
            return Response([])
