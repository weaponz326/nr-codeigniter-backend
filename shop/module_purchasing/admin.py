from django.contrib import admin

from .models import Purchasing, PurchasingItem


# Register your models here.

class PurchasingAdmin(admin.ModelAdmin):
    list_display = ('id', 'account',  'purchasing_code', 'purchasing_date', 'supplier')

class PurchasingItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'purchasing', 'product', 'quantity')

admin.site.register(Purchasing, PurchasingAdmin)
admin.site.register(PurchasingItem, PurchasingItemAdmin)
