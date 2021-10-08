from facturacionApp.models.producto import Producto
from facturacionApp.models.venta import Venta
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto', 'Proveedor', 'descripcion', 'valorUnitario', 'unidad', 'cantidadExistencia', 'composicion', 'producto']