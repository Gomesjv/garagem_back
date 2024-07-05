from django.db import models    

from core.models import Cor, Acessorio

class Veiculo (models.Model):
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Acessorio = models.ManyToManyField(
        Acessorio, on_delete=models.PROTECT, related_name="veiculos")