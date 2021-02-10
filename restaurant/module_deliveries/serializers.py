from rest_framework import serializers

from .models import Delivery
from module_orders.models import Order


# order to be merged into delivery serializer

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'restaurant', 'order_code', 'order_date', 'customer_name', 'order_status']

class DeliverySerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Delivery
        fields = ['id', 'restaurant', 'order', 'delivery_code', 'delivery_date', 'delivery_status']

# for saving delivery order with ids
# to prevent saving with dictionary        
class DeliverySaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['id', 'restaurant', 'order', 'delivery_code', 'delivery_date', 'delivery_status']
