from core.comesc.models import Roll
from rest_framework import serializers

class RollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll
        fields = '__all__'
        