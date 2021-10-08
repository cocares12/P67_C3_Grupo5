from facturacionApp.models.venta import Venta
from facturacionApp.models.usuario import Usuario
from facturacionApp.models.cliente import Cliente
from facturacionApp.models.producto import Producto
from facturacionApp.models.proveedor import Proveedor
from rest_framework import serializers
from facturacionApp.serializers.usuarioSerializer import UsuarioSerializer
from facturacionApp.serializers.clienteSerializer import ClienteSerializer
from facturacionApp.serializers.productoSerializer import ProductoSerializer
from facturacionApp.serializers.proveedorSerializer import ProveedorSerializer

class VentaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    cliente = ClienteSerializer()
    producto =  ProductoSerializer()
    class Meta:
        model = Venta
        fields = ['idVenta', 'fechaVenta', 'cantidadProducto','impuesto', 'subtotal', 'totalVenta','descuento', 'formaPago', 'usuario', 'cliente', 'producto']

        def create(self, validated_data):
            usuarioData = validated_data.pop('usuario')
            clienteData = validated_data.pop('cliente')
            productoData = validated_data.pop('prodcuto')
            ventaInstance = Venta.objects.create(**validated_data)
            Usuario.objects.create(venta=ventaInstance, **usuariotData)
            Cliente.objects.create(venta=ventaInstance, **clientetData)
            Prodcuto.objects.create(venta=ventaInstance, **productotData)
            return ventaInstance

        def to_representation(self, obj):
            venta = Venta.objects.get(idVenta=obj.idVenta)
            usuario = Usuario.objects.get(idUsuario=obj.idUsuario)
            cliente = Cliente.objects.get(idCliente=obj.idCliente)
            producto = Producto.objects.get(idProducto=obj.idProducto)
            return {
                    'idVenta': venta.idVenta,
                    'fechaVenta': venta.fechaVenta,
                    'cantidadProducto': venta.cantidadProducto,
                    'impuesto': venta.impuesto,
                    'subtotal': venta.subtotal,
                    'descuento': venta.descuento,
                    'totalVenta': venta.totalVenta,
                    'formaPago': venta.formaPago,
                    'usuario': {
                        'idUsuario': usuario.idProducto,
                        'username': usuario.username,
                        'password': usuario.password,
                        'tipoUsuario': usuario.tipoUsuario,
                        'nombreUsuario': usuario.nombreUsuario,
                        'apellidoUsuario': usuario.apellidoUsuario
                    },
                    'cliente': {
                        'idCliente': cliente.idCliente,
                        'nombreCliente': cliente.nombreCliente,
                        'apellidoCliente': cliente.apellidoCliente,
                        'correoCliente': cliente.correoCliente
                    },
                    'producto': {
                        'idProducto': producto.idProducto,
                        'descripcion': producto.descripcion,
                        'valorUnitario': producto.valorUnitario,
                        'unidad': producto.unidad,
                        'cantidadExistencia': producto.cantidadExistencia,
                        'composicion': producto.composicion,
                        'proveedor': {
                            'idProveedor': proveedor.idProveedor,
                            'nombreProveedor': proveedor.nombreProveedor,
                            'direccionProveedor': proveedor.direccionProveedor,
                            'numeroTelefonicoProveedor': proveedor.numeroTelefonicoProveedor
                        }
                    }
            }
