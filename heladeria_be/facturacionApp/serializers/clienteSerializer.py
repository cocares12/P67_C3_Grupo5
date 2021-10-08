from facturacionApp.models.cliente import Cliente
from facturacionApp.models.venta import Venta
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['idCliente', 'nombreCliente', 'apellidoCliente', 'correoCliente', 'cliente']