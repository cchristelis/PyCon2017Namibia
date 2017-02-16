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
            'conference',
            'home'
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        layout = Layout(
            Fieldset(
                'Add Visitor',
                Field('name', css_class="form-control"),
                Field('date_left', css_class="form-control", type="date"),
                Field('conference', css_class="form-control"),
                Field('home', css_class="form-control"),
                css_id='visitor-add-form')
        )
        self.helper.layout = layout
        self.helper.html5_required = False
        super(VisitForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit('submit', 'Submit'))
