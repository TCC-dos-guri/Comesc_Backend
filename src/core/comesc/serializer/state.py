from core.comesc.models import State
from rest_framework.serializers import ModelSerializer

class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'