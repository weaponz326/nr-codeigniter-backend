from django.contrib import admin

from .models import Equipment


# Register your models here.

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'equipment_code', 'equipment_name', 'category', 'serial_number', 'condition')

admin.site.register(Equipment, EquipmentAdmin)
