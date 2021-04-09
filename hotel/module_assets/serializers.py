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
            'brand', 
            'model', 
            'purchased_date', 
            'location', 
            'description', 
            'condition', 
        ]
