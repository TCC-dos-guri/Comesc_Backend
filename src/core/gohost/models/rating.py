from django.db import models
from core.usuario.models import Usuario as User
from .hotel import Hotel

class Rating(models.Model):
    rate = models.IntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='ratings')
    
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'