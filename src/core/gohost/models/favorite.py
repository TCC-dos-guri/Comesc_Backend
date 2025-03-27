from django.db import models
from core.usuario.models import Usuario as User
from .hotel import Hotel

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorites')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_favorites')
    
    def __str__(self):
        return f'{self.user} - {self.hotel}'
    
    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'