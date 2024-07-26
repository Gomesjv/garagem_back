from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import VeiculoSerializer, VeiculoWriteSerializer

class VeiculoViewSet (ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return VeiculoWriteSerializer
        return VeiculoSerializer
