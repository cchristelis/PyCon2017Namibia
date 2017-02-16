# -*- coding: utf-8 -*-
import json
from django.views.generic import (
    TemplateView
)

from pycon.models.visit import Visit
from pycon.serializers.visit_serializer import VisitSerializer
from django.views.generic.edit import CreateView
from django import forms


__author__ = 'Dimas Ciputra <dimas@kartoza.com>'
__date__ = '16/02/17'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class VisitorCreate(CreateView):
    model = Visit
    fields = '__all__'
    widgets = {
        'date_left': DateTimeInput()
    }
    template_name = 'visitor/visit_form.html'

class VisitorMapView(TemplateView):
    """Map view for Visitor."""
    template_name = 'visitor/map_page.html'

    def get_context_data(self, **kwargs):
        """Get the context data which is passed to a template.

        :param kwargs: Any arguments to pass to the superclass.
        :type kwargs: dict

        :returns: Context data which will be passed to the template.
        :rtype: dict
        """
        context = super(VisitorMapView, self).get_context_data(**kwargs)
        serializer = VisitSerializer(Visit.objects.all(), many=True)
        visitor = json.dumps(serializer.data)
        context['visitors'] = visitor
        return context
