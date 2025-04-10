from core.comesc.models import Address, State
from rest_framework.serializers import ModelSerializer, SlugRelatedField

class AddressSerializer(ModelSerializer):
    state = SlugRelatedField(slug_field='state', queryset=State.objects.all())
    class Meta:
        model = Address
        fields = '__all__'
