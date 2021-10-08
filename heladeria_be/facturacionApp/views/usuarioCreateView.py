from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from facturacionApp.serializers.usuarioSerializer import UsuarioSerializer

class UsuarioCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"idUsuario":request.data["idUsuario"],"username":request.data["username"],"password":request.data["password"],"tipoUsuario":request.data["tipoUsuario"],"nombreUsuario":request.data["nombreUsuario"],"apellidoUsuario":request.data["apellidoUsuario"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)