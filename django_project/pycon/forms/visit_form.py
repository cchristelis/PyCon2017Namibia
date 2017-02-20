from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Fieldset,
    Submit,
    Field,
)
from pycon.models.visit import Visit


class VisitForm(forms.ModelForm):

    class Meta:
        model = Visit
        fields = (
            'name',
            'date_left',
            'home',
            'conference',
            'gravatar'
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        layout = Layout(
            Fieldset(
                'Add Delegate',
                Field('name', css_class="form-control"),
                Field('date_left', css_class="form-control", type="date"),
                Field('conference', css_class="form-control"),
                Field('gravatar', css_class="form-control"),
                css_id='visitor-add-form')
        )
        self.helper.layout = layout
        self.helper.html5_required = False
        super(VisitForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        instance = super(VisitForm, self).save(commit=False)
        instance.save()
        return instance

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data
