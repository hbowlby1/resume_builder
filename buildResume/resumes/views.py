from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView
from django.conf import settings

from django_weasyprint import WeasyTemplateView
import logging

from .models import (Person, Education, Jobs, Skills, Certificates)
from .forms import (SchoolForm, PersonForms, JobForm, SkillForm, CertForm)

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

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
          return HttpResponse()
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

def createJob(request, pk):
    person = Person.objects.get(id=pk)
    jobs = Jobs.objects.filter(person=person)
    jobForm = JobForm(request.POST or None)

    if request.method == "POST":
        if jobForm.is_valid():
            job = jobForm.save(commit=False)
            job.person = person
            job.save()
            return HttpResponse('\njob saved')
        else:
            return render(request, "partials/job_form.html", context={
                "jobForm": jobForm
            })
        
    context ={
        "jobForm": jobForm,
        "person": person,
        "job": jobs,
    }

    return render(request, "create-job.html", context)

def createJobForm(request):
    jobForm = JobForm()
    context = {
        'jobForm': jobForm
    }
    return render(request, 'partials/job_form.html', context)

def createSkills(request, pk):
    person = Person.objects.get(id=pk)
    skills = Skills.objects.filter(person=person)
    skillForm = SkillForm(request.POST or None)

    if request.method == "POST":
        if skillForm.is_valid():
            skill = skillForm.save(commit=False)
            skill.person = person
            skill.save()
            return HttpResponse(f"skill saved-")
        else:
            return render(request, "partials/skill_form.html", context={
                "skillForm": skillForm
            })
        
    context ={
        "skillForm": skillForm,
        "person": person,
        "skill": skills,
    }

    return render(request, "create-skill.html", context)

def createSkillForm(request):
    skillForm = SkillForm()
    context = {
        'skillForm': skillForm
    }
    return render(request, 'partials/skill_form.html', context)

def createCert(request, pk):
    person = Person.objects.get(id=pk)
    cert = Certificates.objects.filter(person=person)
    certForm = CertForm(request.POST or None)

    if request.method == "POST":
        if certForm.is_valid():
            cert = certForm.save(commit=False)
            cert.person = person
            cert.save()
            return HttpResponse(f"Certificate saved-")
        else:
            return render(request, "partials/cert_form.html", context={
                "certForm": certForm
            })
        
    context ={
        "certForm": certForm,
        "person": person,
        "certificate": cert,
    }

    return render(request, "create_cert.html", context)

def createCertForm(request):
    certForm = CertForm()
    context = {
        'certForm': certForm
    }
    return render(request, 'partials/cert_form.html', context)

# pdf generation
# def getUserData(request, pk):
#     #get all of the objects and connect
#     getPerson = Person.objects.get(id=pk)
#     getEducation = Education.objects.filter(person=getPerson).values()
#     getJobs = Jobs.objects.filter(person=getPerson).values()
#     getSkills = Skills.objects.filter(person=getPerson).values()
#     getCerts = Certificates.objects.filter(person=getPerson).values()

#     #context that holds all of the user data
#     context = {
#         'person': getPerson,
#         'education': getEducation,
#         'jobs': getJobs,
#         'skills': getSkills,
#         'certs': getCerts
#     }
    
#     return render(request, 'pdf-view.html', context)
    
class PDFGenerator(WeasyTemplateView):
    template_name = 'pdf-view.html'
    pdf_stylesheets = [
        settings.STATIC_ROOT + '/css/resume-styles.css',
    ]
    def get_context_data(self, *args, **kwargs):
        context = super(PDFGenerator, self).get_context_data(**kwargs)
        context['person'] = Person.objects.get(id=kwargs['pk'])
        context['education'] = Education.objects.filter(person=context['person']).values()
        context['jobs'] = Jobs.objects.filter(person=context['person']).values()
        context['skills'] = Skills.objects.filter(person=context['person']).values()
        context['certs'] = Certificates.objects.filter(person=context['person']).values()
        return context

    def get_pdf_filename(self):
        return