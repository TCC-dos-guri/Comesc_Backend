from django.db import models
from .supplier import Supplier

class Batch(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='batch')
    qtd = models.IntegerField(default=12)
    kg = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    invoice = models.IntegerField(default=000000)
    class Status(models.TextChoices):
        PENDENTE = 'pendente', "Pendente"
        EM_ESTOQUE = 'em estoque', "Em estoque"
        COM_DEFEITO = 'com defeito', "Com defeito"
        EM_TRANSPORTE = 'em transporte', "Em transporte"

    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDENTE)
    
    def __str__(self):
        return f'{self.supplier.name} - {self.qtd}'