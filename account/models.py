from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Profile(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return f'Profile of {self.username}'

    
    def get_absolute_url(self):
        return reverse('profile', args=[self.slug])



