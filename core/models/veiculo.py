from django.db import models    

from core.models import Cor, Acessorio, Modelo

class Veiculo (models.Model):
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Acessorio = models.ManyToManyField(
        Acessorio,related_name="veiculos")
    def __str__ (self):
        return f"{self.modelo} ({self.ano}) {self.cor}"