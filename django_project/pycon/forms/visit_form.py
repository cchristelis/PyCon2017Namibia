from django import forms

from models.visit import Visit

class VisitForm(forms.ModelForm):


    class Meta:
        model = Visit