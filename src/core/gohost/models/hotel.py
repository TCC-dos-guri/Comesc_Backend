from django.db import models
from core.uploader.models import Image
from core.usuario.models import Usuario as User
from .category import Category

class Hotel(models.Model):
    covers = models.ManyToManyField(Image, related_name='hotel')
    title = models.CharField(max_length=100, null=True, blank=True)
    guests = models.IntegerField(default=1)
    rooms = models.IntegerField(default=1)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='hotel')
    rate = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    class TypeChoices(models.TextChoices):
        HOTEL = 'hotel', 'Hotel'
        POUSADA = 'pousada', 'Pousada',
        CASA = 'casa', 'Casa'
        RESORT = 'resort', 'Resort',
        CAMPINGS = 'campings', 'Campings'

    type = models.CharField(max_length=10, choices=TypeChoices.choices, default=TypeChoices.HOTEL)

    def __str__(self):

        return self.title

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'