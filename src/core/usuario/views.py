from core.usuario.models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def me(self, req):
        user = req.user
        serializer = UsuarioSerializer(user).data
        return Response(data=serializer, status=status.HTTP_200_OK)


    
    

        



