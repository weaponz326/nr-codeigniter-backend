from rest_framework import serializers

from .models import StockItem


class StockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItem
        fields = ['id', 'item_code', 'item_name', 'category', 'item_type', 'quantity', 'refill_ordered']
