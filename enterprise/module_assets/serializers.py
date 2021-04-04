from rest_framework import serializers

from .models import Asset


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'id', 
            'asset_code',
            'asset_name',
            'asset_type',
            'category',
            'date_purchased',
            'purchased_value',
            'supplier',
            'brand',
            'model',
            'serial_number',
            'location',
            'description',
            'condition',
        ]

