from rest_framework import serializers

from .models import Order, OrderItem
from module_menu.models import MenuItem



class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'order_code', 'order_date', 'customer_name', 'order_type', 'order_status']

# menu item to merged into order item

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['id', 'item_code', 'category', 'price']

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'item_code', 'quantity']

