from django.contrib import admin

from .models import Order


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'order_code', 'order_date', 'product', 'quantity', 'order_status')

admin.site.register(Order, OrderAdmin)
