from core.comesc.models import Roll
from core.comesc.serializer import RollSerializer
from rest_framework.viewsets import ModelViewSet

class RollViewSet(ModelViewSet):
    queryset = Roll.objects.all()
    serializer_class = RollSerializer