from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Veiculo

from uploader.models import Image
from uploader.serializers import ImageSerializer

class VeiculoSerializer (ModelSerializer):
    foto_veiculo_attachment_key = SlugRelatedField(
        source="foto_veiculo",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto_veiculo = ImageSerializer(required=False, read_only=True)
    class Meta :
        model = Veiculo
        fields = "__all__"
