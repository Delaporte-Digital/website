from django.db import models

# Create your models here.
class Company(models.Model):
    provider = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    logo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    employees = models.IntegerField()
    location = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    founders = models.ForeignKey('Founder', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Founder(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/')
    linkedin = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name