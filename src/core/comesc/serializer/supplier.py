from rest_framework import serializers
from core.comesc.models import Supplier, Address, State
from .address import AddressSerializer

class SupplierCreateSerializer(serializers.ModelSerializer):
    # Para leitura: mostra os dados completos do endereço
    address = AddressSerializer(read_only=True)
    # Para escrita: envia apenas o ID do endereço
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        source='address',  # aponta para o campo address do modelo
        write_only=True
    )

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'cnpj', 'address', 'address_id']

    def create(self, validated_data):
        # Aqui address já vem como objeto Address via PrimaryKeyRelatedField
        address_obj = validated_data.pop('address')
        supplier = Supplier.objects.create(address=address_obj, **validated_data)
        return supplier


class SupplierSerializer(serializers.ModelSerializer):
    # Apenas leitura, mostra detalhes do address e state
    address = AddressSerializer()
    
    class Meta:
        model = Supplier
        fields = '__all__'
        depth = 2

class SupplierUpdateSerializer(serializers.ModelSerializer):
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        source='address',
        required=False
    )

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'cnpj', 'address_id']
