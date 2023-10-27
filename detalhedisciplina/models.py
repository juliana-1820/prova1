from django.db import models

# Create your models here.
class detalhedisciplina(models.Model):
    codigo = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
   