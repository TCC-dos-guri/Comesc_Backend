from django.contrib import admin
from core.comesc.models import Supplier

@admin.register(Supplier)
class AdminSupplier(admin.ModelAdmin):
    list_display = ('name', 'cnpj',)
    search_fields = ('name', 'cnpj', )
    