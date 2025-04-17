from core.comesc.models import Roll
from rest_framework import serializers

class RollCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll
        fields = ['production_order', 'color', 'material', 'kg', 'batch', 'nonconformity']

class RollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll
        fields = '__all__'
        depth = 2
        