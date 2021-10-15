from facturacionApp.models.usuario import Usuario
from facturacionApp.models.venta import Venta
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario', 'username', 'password','tipoUsuario', 'nombreUsuario', 'apellidoUsuario']