from django.contrib import admin
from .models import Procurement


# Register your models here.

class ProcurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_code', 'order_type', 'order_date', 'account')

admin.site.register(Procurement, ProcurementAdmin)
