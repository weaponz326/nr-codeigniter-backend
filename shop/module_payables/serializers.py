from rest_framework import serializers

from .models import Payable


class PayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payable
        fields = [
            'id', 
            'payable_code', 
            'payable_date', 
            'due_date', 
            'invoice_number', 
            'customer_name',
            'amount',
            'date_paid'
        ]
