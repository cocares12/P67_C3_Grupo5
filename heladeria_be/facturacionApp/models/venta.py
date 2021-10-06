from django.db import models

class Venta(models.Models):
    idVenta = models.BigAutoField(primary_key=True)
    fechaVenta = models.DateTimeField('Fecha_Venta')
    cantidadProducto = models.BigIntegerField('Cantidad_Producto')
    impuesto = models.DecimalField('IVA')
    subtotal = models.DecimalField('Subtotal')
    totalVenta = models.DecimalField('Total')
    
