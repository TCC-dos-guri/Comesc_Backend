from django.db import models

from ...usuario.models import Usuario as User
from . import Roll

class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll = models.ForeignKey(Roll, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user
    
        
        