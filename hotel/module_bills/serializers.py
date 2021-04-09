from rest_framework import serializers

from .models import Bill, RoomBill, ServiceBill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'bill_code', 'bill_date']

class RoomBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBill
        fields = ['id', 'amount']

class ServiceBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBill
        fields = ['id', 'number_nights', 'amount']
