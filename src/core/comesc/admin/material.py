from django.contrib import admin
from core.comesc.models import Material

@admin.register(Material)
class AdminMaterial(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('-id', )