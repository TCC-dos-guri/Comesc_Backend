from core.comesc.models import State
from core.comesc.serializer import StateSerializer
from rest_framework.viewsets import ModelViewSet

class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
