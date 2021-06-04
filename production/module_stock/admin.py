from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import StockItem


# Register your models here.

class StockItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'material', 'quantity')

admin.site.register(StockItem, StockItemAdmin)
