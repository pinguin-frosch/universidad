from django.db import models

class Persona(models.Model):
    run = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    direccion = models.CharField(max_length=150)
    comentario = models.CharField(max_length=150, null=True)
    fono = models.CharField(max_length=15)