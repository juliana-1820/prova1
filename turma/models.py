from django.db import models

# Create your models here.
class turma(models.Model):
    codigo = models.CharField(max_length=100)
    codigocurso= models.CharField(max_length=100)
   