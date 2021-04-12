from rest_framework import serializers

from .models import Purchasing, PurchasingItem


class PurchasingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchasing
        fields = ['id', 'purchasing_number', 'purchasing_date', 'supplier_invoice']
