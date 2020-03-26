from django.db import models

# Create your models here.
class Materia(models.Model):
    nombreMateria = models.CharField(max_length=254, null=False)

class Alumno(models.Model):
    Materia = models.ForeignKey(Materia,on_delete = models.CASCADE)
    name = models.CharField(max_length=254, null=False)
    carrera = models.CharField(max_length=254, null=False)
    edad = models.IntegerField(null=False)
    direccion =  models.CharField(max_length=254, null=False)
    genero =  models.CharField(max_length=254, null=False)
    matricula =  models.CharField(max_length=254, null=False)