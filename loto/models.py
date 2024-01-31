from django.db import models

# Create your models here.
class Links(models.Model):
    link = models.URLField

    def __str__(self):
        return self.link


class Data(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=250)
    resultados = models.ImageField(upload_to='img', blank=True)
    ganadores = models.ImageField(upload_to='img', blank=True)
    # fecha = models.DateTimeField()
    # lista = 
    # boleano = models.BooleanField(default=False)
    # alternativas = 

    def __str__(self):
        return self.url
