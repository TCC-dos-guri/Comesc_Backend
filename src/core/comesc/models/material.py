from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100, unique=True)
    composition = models.CharField(max_length=100, verbose_name='Composition', blank=True, null=True)
    yarn_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Yarn Cost', blank=True, null=True)
    knitting_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Knitting Cost', blank=True, null=True)
    dyeing_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Dyeing Cost', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
    
    @property
    def cost(self):
        return self.yarn_cost + self.knitting_cost + self.dyeing_cost 
    