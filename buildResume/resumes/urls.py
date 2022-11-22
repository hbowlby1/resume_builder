from django.urls import path

from .views import (HomePageView, 
createSchool, 
createPerson,
createSchoolForm,)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('person/', createPerson, name='person'),
    path('person/<pk>/school/', createSchool, name='create-school'),
    path('htmx/create-school-form', createSchoolForm, name='create-school-form'),

]
