from django.db import models
from categorias.models import Categoria
from marcas.models import Marca


class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
