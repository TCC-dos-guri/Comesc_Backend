from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Usuario, Worker


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

