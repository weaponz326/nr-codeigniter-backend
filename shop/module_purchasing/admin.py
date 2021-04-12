from django.contrib import admin

from .models import Purchasing, PurchasingItem


# Register your models here.

class PurchasingAdmin(admin.ModelAdmin):
    list_display = ('id', 'account',  'purchasing_number', 'purchasing_date', 'supplier')

class PurchasingItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'purchasing', 'product', 'quantity', 'total_price')

admin.site.register(Purchasing, PurchasingAdmin)
admin.site.register(PurchasingItem, PurchasingItemAdmin)
