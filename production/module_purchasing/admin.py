from django.contrib import admin

from .models import Purchasing, PurchasingItem


# Register your models here.

class PurchasingAdmin(admin.ModelAdmin):
    list_display = ('id', 'account',  'purchasing_code', 'purchasing_date', 'supplier_name')

class PurchasingItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'purchasing', 'item_description', 'quantity')

admin.site.register(Purchasing, PurchasingAdmin)
admin.site.register(PurchasingItem, PurchasingItemAdmin)
