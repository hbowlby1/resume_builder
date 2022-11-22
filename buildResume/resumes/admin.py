from django.contrib import admin

from .models import (Person, Education)
# Register your models here.
class SchoolInlineAdmin(admin.TabularInline):
    model = Education

class PersonAdmin(admin.ModelAdmin):
    inlines = [SchoolInlineAdmin]

admin.site.register(Person)
admin.site.register(Education)
