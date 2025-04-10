from core.comesc.models import Supplier
from core.comesc.serializer import SupplierSerializer   
from rest_framework.viewsets import ModelViewSet

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer