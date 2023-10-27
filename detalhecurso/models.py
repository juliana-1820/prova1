from django.db import models

# Create your models here.
class detalhecurso(models.Model):
    curso = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    