from django.db import models
from .proveedor import Proveedor

class Producto(models.Model):
    idProducto = models.BigIntegerField(primary_key=True)
    Proveedor = models.ForeignKey(Proveedor, related_name='Proveedor', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)
    valorUnitario = models.DecimalField('Valor unitario',  max_digits=5, decimal_places=2)
    unidad = models.CharField("Unidad del producto", max_length = 20)
    cantidadExistencia = models.DecimalField('Existencia',  max_digits=5, decimal_places=2)
    composicion = models.CharField("Composición", max_length = 50)
