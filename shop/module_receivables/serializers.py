from rest_framework import serializers

from .models import Receivable


class ReceivableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receivable
        fields = [
            'id', 
            'receivable_code', 
            'receivable_date', 
            'due_date', 
            'invoice_number', 
            'customer_name',
            'amount',
            'date_received'
        ]
