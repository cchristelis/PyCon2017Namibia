from __future__ import unicode_literals

from django.contrib.gis.db import models


class Visit(models.Model):
    name = models.CharField(max_length=200)
    home = models.PointField(null=True, blank=True)
    date_left = models.DateTimeField()
    gravatar = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % (self.name)
