from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from facturacionApp.serializers.ventaSerializer import VentaSerializer

class VentaCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = VentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"idVenta":request.data["idVenta"],"usuario":request.data["usuario"],"cliente":request.data["cliente"],"producto":request.data["producto"],"fechaVenta":request.data["fechaVenta"],"cantidadProducto":data.request["cantidadProducto"],"impuesto":data.request["impuesto"],"subtotal":data.request["subtotal"],"totalVenta":data.request["totalVenta"],"descuento":data.request["descuento"],"formaPago":["formaPago"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)