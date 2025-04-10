from core.comesc.models import Supplier, Address, State
from rest_framework.serializers import ModelSerializer
from .address import AddressSerializer

class SupplierCreateSerializer(ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Supplier
        fields = '__all__'
    
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        state_data = validated_data.pop('state')

        state_obj = State.objects.get(**state_data)
        address_obj = Address.objects.create(state=state_obj, **address_data)

        supplier = Supplier.objects.create(address=address_obj, **validated_data)
        return supplier
    
class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        depth = 2
    


