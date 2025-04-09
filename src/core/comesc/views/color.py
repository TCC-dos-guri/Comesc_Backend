from core.comesc.models import Color
from core.comesc.serializer import ColorSerializer
from rest_framework.viewsets import ModelViewSet

class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer