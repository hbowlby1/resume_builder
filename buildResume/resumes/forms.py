from django import forms

from .models import (Person, Education)

class PersonForms(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
            'street',
            'city',
            'state',
            'zipCode',
        ]

class SchoolForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = (
            'school_name',
            'city',
            'state',
            'major',
            'year_start',
            'year_graduated',
        )