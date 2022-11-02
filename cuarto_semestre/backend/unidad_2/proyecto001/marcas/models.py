from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
