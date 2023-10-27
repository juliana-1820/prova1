from django.db import models

# Create your models here.
class aluno(models.Model):
    nome = models.CharField(max_length=100)
    sexo= models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    datanascimento=models.DateField