from rest_framework import serializers
from core.comesc.models import Batch

class BatchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['id', 'supplier', 'color', 'material', 'kg', 'roll']
        
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
        depth = 2