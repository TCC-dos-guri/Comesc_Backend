from core.comesc.models.batch import Batch
from core.comesc.models.roll import Roll
from core.comesc.serializer.roll import RollSerializer
from core.comesc.serializer.batch import BatchSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ReportView(APIView):
    def get(self, request, id):
        batch = Batch.objects.get(id=id)
        batch_rolls = Roll.objects.filter(batch=batch)
        batch_data = BatchSerializer(batch).data
        rolls_data = RollSerializer(batch_rolls, many=True).data

        final_data = {
            'batch': batch_data,
            'rolls': rolls_data
        }


        return Response(final_data, status=status.HTTP_200_OK)
    