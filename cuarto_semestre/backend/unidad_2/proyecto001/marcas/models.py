from django.db import models


class MarcaModel(models.Model):
    nombre = models.CharField(max_length=15)
