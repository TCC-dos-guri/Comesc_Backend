from core.comesc.models import Supplier
from rest_framework.serializers import ModelSerializer

class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
