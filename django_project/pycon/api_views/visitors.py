__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '16/02/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

from rest_framework.views import APIView
from rest_framework.response import Response
from pycon.models.conference_visit_entry import  Visit
from pycon.serializers.conference_visit_entry_serializer import VisitSerializer


class VisitorsApi(APIView):
    def get(self, request, conference_id=None):
        if conference_id:
            visitors = Visit.objects.filter(conference=conference_id)
            serializer = VisitSerializer(visitors,many=True)
            return Response(serializer.data)
        else:
            return Response([])
