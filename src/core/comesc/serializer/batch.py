from core.comesc.models import Batch
from rest_framework.serializers import ModelSerializer

class BatchCreateSerializer(ModelSerializer):
    class Meta:
        model = Batch
        fields = ['supplier', 'qtd', 'kg', 'price', 'invoice']

class BatchSerializer(ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
        depth = 2