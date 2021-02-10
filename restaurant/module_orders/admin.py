from django.contrib import admin

from .models import Order, OrderItem


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'order_code', 'order_date', 'customer_name', 'order_status')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'menu_item', 'quantity')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
