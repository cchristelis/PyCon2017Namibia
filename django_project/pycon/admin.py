# coding=utf-8
__author__ = 'Muhammad Anis <anisiconic@gmail.com>'
__date__ = '18/11/16'

from django.contrib.gis import admin
from models.conference_visit_entry import ConferenceVisitEntry
from models.conference import *
from models.visit import *

admin.site.register(ConferenceVisitEntry, admin.ModelAdmin)
admin.site.register(Conference, admin.ModelAdmin)
admin.site.register(Visit, admin.ModelAdmin)