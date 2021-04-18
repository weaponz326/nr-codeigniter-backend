from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 
            'product_code', 
            'product_name', 
            'product_type', 
            'description', 
            'version', 
            'model_number', 
        ]
