from django.db import models
from .usuario import Usuario
from .cliente import Cliente
from .producto import Producto

class Venta(models.Model):
    idVenta = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name='usuario', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='cliente', on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='producto', on_delete = models.CASCADE)
    fechaVenta = models.DateTimeField('Fecha de venta')
    cantidadProducto = models.BigIntegerField('Cantidad del producto')
    impuesto = models.DecimalField('IVA', max_digits=6, decimal_places=1)
    subtotal = models.DecimalField('Subtotal', max_digits=5, decimal_places=1)
    totalVenta = models.DecimalField('Total',  max_digits=6, decimal_places=1)
    
    POSIBILIDAD_DE_DESCUENTO = [
    ('SI', 'Aplica'),
    ('NO', 'No aplica'),    
    ]
    descuento = models.CharField(
        max_length = 2,
        choices = POSIBILIDAD_DE_DESCUENTO,
        default = 'NO',
    )

    FORMA_DE_PAGO=[
        ('EF','Efectivo'),
        ('TD', 'Tarjeta débito'),
        ('TC', 'Tarjeta de crédito'),
    ]
    formaPago = models.CharField(
        max_length = 2,
        choices =   FORMA_DE_PAGO,
        default = 'EF',
    )