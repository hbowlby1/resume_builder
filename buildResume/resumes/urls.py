from django.urls import path

from .views import (HomePageView,
AboutPageView, 
createSchool, 
createPerson,
createSchoolForm,
createJob,
createJobForm,
createSkills,
createSkillForm,
createCert,
createCertForm,
PDFGenerator,)

from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('person/', createPerson, name='person'),
    path('person/<int:pk>/school/', createSchool, name='create-school'),
    path('person/<int:pk>/jobs/', createJob, name='create-job'),
    path('person/<int:pk>/skills/', createSkills, name='create-skill'),
    path('person/<int:pk>/certs/', createCert, name='create-cert'),

    #HTMX
    path('htmx/create-school-form', createSchoolForm, name='create-school-form'),
    path('htmx/create-job-form', createJobForm, name='create-job-form'),
    path('htmx/create-skill-form', createSkillForm, name='create-skill-form'),
    path('htmx/create-cert-form', createCertForm, name='create-cert-form'),

    #PDF generation
    path('<int:pk>/pdf/create', PDFGenerator.as_view(), name='create-pdf'),

]
