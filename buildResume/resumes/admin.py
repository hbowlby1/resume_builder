from django.contrib import admin

from .models import (Person, Education, Jobs)
# Register your models here.
class SchoolInlineAdmin(admin.TabularInline):
    model = Education

class JobInlineAdmin(admin.TabularInline):
    model = Jobs
class PersonAdmin(admin.ModelAdmin):
    inlines = [SchoolInlineAdmin, JobInlineAdmin]



admin.site.register(Person)
admin.site.register(Education)
admin.site.register(Jobs)
