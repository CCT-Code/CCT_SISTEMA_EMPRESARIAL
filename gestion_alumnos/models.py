from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=150)
    curso = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre