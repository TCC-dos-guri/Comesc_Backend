from django.contrib import admin
from core.comesc.models import Color

@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    list_display = ('name', 'hex', )
    search_fields = ('name', 'hex', )