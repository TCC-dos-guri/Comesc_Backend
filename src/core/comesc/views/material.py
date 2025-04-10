from core.comesc.models import Material
from core.comesc.serializer import MaterialSerializer
from rest_framework.viewsets import ModelViewSet

class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    
