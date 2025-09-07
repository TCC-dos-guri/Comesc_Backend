from django.db import models
from .color import Color
from .batch import Batch


class Roll(models.Model):
    production_order = models.AutoField(primary_key=True, unique=True)
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='+', null=True, blank=True)
    kg = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, default=None, related_name='roll')
    nonconformity = models.BooleanField(default=False)

    def __str__(self):
        return f'pertencente ao lote: {self.batch.id}'

    