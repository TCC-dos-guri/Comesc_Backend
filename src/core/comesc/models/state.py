from django.db import models

class State(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    acronym = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - ({self.acronym})'
    
    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
    