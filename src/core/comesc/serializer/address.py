from core.comesc.models import Address
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .state import StateSerializer

class AddressSerializer(ModelSerializer):
    state = StateSerializer()
    class Meta:
        model = Address
        fields = '__all__'

