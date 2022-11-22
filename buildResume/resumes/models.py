from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.last_name} ({self.id})"

class Education(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    major = models.CharField(max_length=200, blank=True, null=True)
    year_start = models.CharField(max_length=4, help_text='YYYY', null=True, blank=True)
    year_graduated = models.CharField(max_length=4, help_text='YYYY', null=True, blank=True)

