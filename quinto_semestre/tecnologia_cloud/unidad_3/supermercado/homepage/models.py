from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
