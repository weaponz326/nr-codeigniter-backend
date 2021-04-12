from django.contrib import admin

from .models import InventoryItem


# Register your models here.

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'product', 'quantity')

admin.site.register(InventoryItem, InventoryItemAdmin)
