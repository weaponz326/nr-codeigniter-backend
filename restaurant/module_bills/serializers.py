from rest_framework import serializers

from .models import Bill
from module_orders.models import Order
from module_sittings.models import Sitting
from module_deliveries.models import Delivery


# order, sitting, delivery to be merged into bill serializer

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'order_code', 'order_date', 'customer_name']

class SittingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sitting
        fields = ['id', 'sitting_code', 'sitting_date']

class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['id', 'delivery_code', 'delivery_date']

class BillSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    sitting = SittingSerializer()
    delivery = DeliverySerializer()

    class Meta:
        model = Bill
        fields = [
            'id', 
            'order', 
            'delivery', 
            'sitting', 
            'bill_code', 
            'bill_date', 
            'bill_type', 
            'customer_name'
        ]

# for saving bill order,sitting, delivery with ids
# to prevent saving with dictionary        
class BillSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = [
            'id', 
            'order', 
            'delivery', 
            'sitting', 
            'bill_code', 
            'bill_date', 
            'bill_type', 
            'customer_name'
        ]
