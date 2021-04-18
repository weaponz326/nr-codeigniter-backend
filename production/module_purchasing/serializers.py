from rest_framework import serializers

from .models import Purchasing, PurchasingItem


class PurchasingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchasing
        fields = ['id', 'supplier_name', 'supplier_contact', 'purchasing_code', 'purchasing_date', 'supplier_invoice']
