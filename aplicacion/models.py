from django.db import models

# Create your models here.
class Clases(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.nombre} ({self.Codigo_de_clase})"
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Instructores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()


