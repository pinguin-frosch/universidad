from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.PositiveIntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
