from rest_framework import serializers
from core.comesc.models import Batch
from core.comesc.serializer import RollSerializer
from core.uploader.serializers import ImageUploadSerializer, ImageSerializer
from core.uploader.models import Image
from core.comesc.models import Roll

class BatchCreateSerializer(serializers.ModelSerializer):
    roll = RollSerializer(many=True)
    cover = serializers.SlugRelatedField(
        slug_field='attachment_key',
        queryset=Image.objects.all(),
        required=False,
        write_only=True
    )
    class Meta:
        model = Batch
        fields = ['id', 'supplier', 'material', 'composition', 'invoice', 'kg', 'roll', 'cover']

    def create(self, validated_data):
        rolls_data = validated_data.pop('roll')

        batch = Batch.objects.create(**validated_data)

        for roll_data in rolls_data:
            Roll.objects.create(batch=batch, **roll_data)

        return batch
        
class BatchSerializer(serializers.ModelSerializer):
    cover = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Batch
        fields = '__all__'
        depth = 2