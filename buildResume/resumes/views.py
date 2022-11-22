from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.views.generic import TemplateView

from django.urls import reverse_lazy, reverse

from .models import (Person, Education)
from .forms import (SchoolForm, PersonForms)

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def createPerson(request):
    personForm = PersonForms(request.POST or None)

    if request.method == "POST":
        if personForm.is_valid():
            person = personForm.save(commit=False)
            person.save()
            return HttpResponseRedirect(f'/person/{person.id}/school/')
        else:
            return render(request, "person_form.html", context={
                "personForm": personForm
            })

    context = {
        "personForm": PersonForms,
    }

    return render(request, 'person_form.html', context)

def createSchool(request, pk):
    person = Person.objects.get(id=pk)
    schools = Education.objects.filter(person = person)
    schoolForm = SchoolForm(request.POST or None)

    if request.method == "POST":
        if schoolForm.is_valid():
          school = schoolForm.save(commit=False)
          school.person = person
          school.save()
          return HttpResponse("success")
        else:
            return render(request, "partials/school_form.html", context={
                "schoolForm": schoolForm
            })

    context = {
        "schoolForm": schoolForm,
        "person": person,
        "school": schools,
    }

    return render(request, "create_school.html", context)

# form creators
def createSchoolForm(request):
    schoolForm = SchoolForm()
    context = {
        'schoolForm': schoolForm
    }
    return render(request, 'partials/school_form.html', context)