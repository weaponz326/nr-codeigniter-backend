from rest_framework import serializers

from .models import Procurement


class ProcurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurement
        fields = [
            'id', 
            'order_code',
            'order_type',
            'order_date',
            'description',
            'project',
            'recepient',
            'vendor',
            'vendor_phone',
            'vendor_address',
            'vendpr_email',
            'order_status',
        ]

