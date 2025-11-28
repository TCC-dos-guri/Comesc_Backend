from core.comesc.models import Supplier
from core.comesc.serializer import SupplierSerializer, SupplierCreateSerializer, SupplierUpdateSerializer
from rest_framework.viewsets import ModelViewSet

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return SupplierCreateSerializer
        if self.action in ['update', 'partial_update']:
            return SupplierUpdateSerializer
        return SupplierSerializer
