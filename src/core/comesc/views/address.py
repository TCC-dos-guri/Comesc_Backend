from core.comesc.serializer import AddressSerializer
from core.comesc.models import Address
from rest_framework.viewsets import ModelViewSet

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer