from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

class Conference(models.Model):
    conference_name = models.CharField(max_length=200)
    conference_code = models.CharField(max_length=200)