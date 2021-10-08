from facturacionApp.models.proveedor import Proveedor
from facturacionApp.models.producto import Producto
from rest_framework import serializers

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['idProveedor', 'nombreProveedor', 'direccionProveedor', 'numeroTelefonicoProveedor', 'Proveedor']