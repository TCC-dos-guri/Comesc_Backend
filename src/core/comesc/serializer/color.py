from core.comesc.models import Color
from rest_framework.serializers import ModelSerializer

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'