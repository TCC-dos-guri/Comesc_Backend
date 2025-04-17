from core.comesc.models import Batch
from core.comesc.serializer.batch import BatchSerializer, BatchCreateSerializer
from rest_framework.viewsets import ModelViewSet

class BatchViewSet(ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
            return BatchCreateSerializer
        return BatchSerializer