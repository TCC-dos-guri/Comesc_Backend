from core.comesc.models import Batch, Roll
from core.comesc.serializer.batch import BatchSerializer, BatchCreateSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class BatchViewSet(ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
            return BatchCreateSerializer
        return BatchSerializer
    
    def retrieve(self, request, *args, **kwargs):
        batch = self.get_object()
        serializer = self.get_serializer(batch)

        batch_id = kwargs['pk']
        rolls_in_batch = Roll.objects.filter(batch=batch_id, nonconformity=True)
        nonconformity_rolls = len(rolls_in_batch)

        data = serializer.data
        data['nonconformity_rolls'] = nonconformity_rolls

        return Response(data)