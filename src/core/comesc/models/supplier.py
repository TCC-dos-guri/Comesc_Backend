from django.db import models
from .address import Address

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'


    
