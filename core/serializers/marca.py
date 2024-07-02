from rest_framework.serializers import ModelSerializer

from core.models import marca

class MarcaSerializer (ModelSerializer):
    class Meta :
        model = marca
        fields = "__all__"