from django.contrib import admin

from .models import Sales


# Register your models here.

class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'sales_code', 'sales_code', 'product', 'quantity')

admin.site.register(Sales, SalesAdmin)
