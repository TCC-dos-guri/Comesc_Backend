from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=255, unique=True)
    hex = models.CharField(max_length=7, unique=True)
    
    def __str__ (self):
        return self.name