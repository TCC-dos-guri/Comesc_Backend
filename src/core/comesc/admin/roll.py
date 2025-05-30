from django.contrib import admin
from core.comesc.models import Roll

@admin.register(Roll)
class AdminRoll(admin.ModelAdmin):
    list_display = ('production_order', 'get_batch_status',)
    search_fields = ('production_order', 'get_batch_status',)
    list_filter = ('batch__status',)
    ordering = ('-production_order',)

    def get_batch_status(self, obj):
        return obj.batch.status