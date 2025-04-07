from django.contrib import admin
from core.comesc.models import Roll

@admin.register(Roll)
class AdminRoll(admin.ModelAdmin):
    list_display = ('ordem_producao', 'status',)
    search_fields = ('ordem_producao', 'status',)
    list_filter = ('status',)
    ordering = ('-ordem_producao',)