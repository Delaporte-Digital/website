from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='project_post')
    logo = models.ImageField(upload_to='projects/', blank=True)
    raised = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title