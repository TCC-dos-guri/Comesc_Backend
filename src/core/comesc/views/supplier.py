from core.comesc.models import Supplier
from core.comesc.serializer import SupplierSerializer, SupplierCreateSerializer  
from rest_framework.viewsets import ModelViewSet

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return SupplierCreateSerializer
        return SupplierSerializer