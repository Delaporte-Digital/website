from django.db import models

# Create your models here.
class Job(models.Model):
    class Provider(models.IntegerChoices):
        WELLFOUND = 1
        REMOTEOK = 2
        REMOTIVE = 3
        WEWORKREMOTELY = 4
        JOBSINDEV = 5
        STACKOVERFLOW = 6
        GITHUB = 7
        ANGELLIST = 8
        LANDINGJOBS = 9
        WORKINGNOMADS = 10
        REMOTELY = 11
    provider = models.IntegerField(choices=Provider.choices)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    remote = models.BooleanField()
    experience = models.CharField(max_length=100)
    visa_sponsorship = models.BooleanField()
    hires_remotely_in = models.CharField(max_length=100)
    relocation = models.CharField(max_length=100)
    hiring_contacts = models.CharField(max_length=100)
    description = models.TextField()