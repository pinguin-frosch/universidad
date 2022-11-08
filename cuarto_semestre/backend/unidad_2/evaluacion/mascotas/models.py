from django.db import models
from tipos.models import Tipo


class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.ForeignKey(Tipo, on_delete=models.RESTRICT)
