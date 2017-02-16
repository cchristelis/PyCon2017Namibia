from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Conference(models.Model):
    conference_name = models.CharField(max_length=200)
    conference_code = models.CharField(max_length=200)

class Visit(models.Model):
    name = models.CharField(max_length=200)
    home = models.PointField(null=True,blank=True)
    date_left = models.DateTimeField()
    gravatar = models.URLField


