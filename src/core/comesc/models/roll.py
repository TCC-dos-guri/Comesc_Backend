from django.db import models
from .material import Material
from .color import Color
from .batch import Batch


class Roll(models.Model):
    ordem_producao = models.IntegerField(primary_key=True, unique=True)
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='+')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='roll')
    kg = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, default=None, related_name='roll')
    class Status(models.TextChoices):
        PENDENTE = 'pendente', "Pendente"
        EM_ESTOQUE = 'em estoque', "Em estoque"
        COM_DEFEITO = 'com defeito', "Com defeito"

    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDENTE)

    def __str__(self):
        return f'pertencente ao lote: {self.batch.id}'

    