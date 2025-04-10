from core.comesc.models import Material
from rest_framework import serializers

class MaterialCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name', 'composition', 'yarn_cost', 'knitting_cost', 'dyeing_cost', 'cost']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'