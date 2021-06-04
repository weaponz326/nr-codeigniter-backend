from rest_framework import serializers

from .models import Bill, RoomBill, ServiceBill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class RoomBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBill
        fields = '__all__'

class ServiceBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBill
        fields = '__all__'
