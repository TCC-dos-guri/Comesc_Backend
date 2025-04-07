from django.contrib import admin
from core.comesc.models import Batch

@admin.register(Batch)
class AdminBatch(admin.ModelAdmin):
    list_display = ("invoice", 'supplier', 'qtd', 'kg', 'price', )
    search_fields = ('invoice', )
    list_filter = ('supplier', 'price')
    ordering = ("-id", )
