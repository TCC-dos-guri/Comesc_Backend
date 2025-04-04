from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    number = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return f'street:{self.street} - {self.number is not None if self.number else ''} - {self.state}'
    
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'