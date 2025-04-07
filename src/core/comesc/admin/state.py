from django.contrib import admin
from core.comesc.models import State

@admin.register(State)
class AdminState(admin.ModelAdmin):
    list_display = ('name', 'acronym',)
    search_fields = ('name', 'acronym',)