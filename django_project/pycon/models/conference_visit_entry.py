__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '16/02/17'

from django.contrib.gis.db import models
from pycon.models.conference import Conference
from pycon.models.visit import Visit


class ConferenceVisitEntry(models.Model):
    """
    Integrated model of relationships between Conference and Visit.
    """

    id = models.AutoField(primary_key=True)
    conference = models.ForeignKey(Conference)
    visit = models.ForeignKey(Visit)

    def __unicode__(self):
        return '%s to %s' % (self.visit.name, self.conference.conference_name)
