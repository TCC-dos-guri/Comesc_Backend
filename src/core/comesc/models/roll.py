from django.db import models
from .material import Material
from .color import Color
from .batch import Batch


class Roll(models.Model):
    production_order = models.IntegerField(primary_key=True, unique=True)
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='+')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='roll')
    kg = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, default=None, related_name='roll')
    nonconformity = models.BooleanField(default=False)

    def __str__(self):
        return f'pertencente ao lote: {self.batch.id}'

    