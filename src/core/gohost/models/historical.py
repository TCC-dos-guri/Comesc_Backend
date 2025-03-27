from django.db import models
from core.usuario.models import Usuario as User
from .hotel import Hotel

class Historical(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='historical', null=True, blank=True, default=None)
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name='historical', null=True, blank=True, default=None)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.hotel.title}'