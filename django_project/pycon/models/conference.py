from __future__ import unicode_literals

from django.contrib.gis.db import models


class Conference(models.Model):
    conference_name = models.CharField(max_length=200)
    conference_code = models.CharField(max_length=200)
    location = models.PointField(null=True, blank=True)
    logo    = models.ImageField(null=True,blank=True)

    def __unicode__(self):
        return '[%s] %s' % (self.conference_code, self.conference_name)
