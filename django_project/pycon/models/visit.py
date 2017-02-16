from __future__ import unicode_literals

from django.contrib.gis.db import models
from pycon.models.conference import  Conference



class Visit(models.Model):
    name = models.CharField(max_length=200)
    home = models.PointField(null=True, blank=True)
    date_left = models.DateTimeField()
    gravatar = models.EmailField(null=True,blank=True)
    conference = models.ForeignKey(Conference,null=False)
    
    def __unicode__(self):
        return '%s' % (self.name)

