from django.contrib import admin

from .models import Supplier


# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'supplier_code', 'phone', 'email')

admin.site.register(Supplier, SupplierAdmin)
