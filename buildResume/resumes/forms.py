from django import forms

from .models import (Person, Education, Jobs, Skills, Certificates)

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

class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = (
            'job_title',
            'employer',
            'year_started',
            'year_end',
            'job_description',
        )

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = (
            'skill_name',
        )

class CertForm(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = (
            'cert_name',
            'cert_url',
            'cert_author',
            'year_awarded',
            'year_expired',
        )