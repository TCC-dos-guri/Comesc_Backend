from rest_framework import serializers
from core.comesc.models import Address
from .state import StateSerializer

class AddressSerializer(serializers.ModelSerializer):
    # Para leitura, mostra o objeto completo
    state = StateSerializer(read_only=True)
    # Para escrita, recebe apenas o ID
    state_id = serializers.PrimaryKeyRelatedField(
        queryset=StateSerializer.Meta.model.objects.all(),
        source='state',  
        write_only=True
    )

    class Meta:
        model = Address
        fields = ['id', 'street', 'cep', 'number', 'state', 'state_id']
