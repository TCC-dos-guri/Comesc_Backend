from django.contrib import admin
from core.comesc.models import Address

@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ("cep",)
    search_fields = ('cep', "street", "number", 'state',)
    ordering = ("-id",)
