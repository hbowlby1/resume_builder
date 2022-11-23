from django.urls import path

from .views import (HomePageView, 
createSchool, 
createPerson,
createSchoolForm,
createJob,
createJobForm,)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('person/', createPerson, name='person'),
    path('person/<int:pk>/jobs/', createJob, name='create-job'),
    path('person/<int:pk>/school/', createSchool, name='create-school'),

    #HTMX
    path('htmx/create-school-form', createSchoolForm, name='create-school-form'),
    path('htmx/create-job-form', createJobForm, name='create-job-form'),

]
