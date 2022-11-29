from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self):
        return self.nombre+ " "+str(self.comision)

class Profesor (models.Model):
    nombre=models.CharField( max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    profesiones=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+ " "+self.apellido

class Estudiantes (models.Model):
    nombre=models.CharField( max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)

    def __str__(self):
        return self.nombre+ " "+self.apellido

class Enregable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField(auto_now=False, auto_now_add=False)
    entregado=models.BooleanField()
    