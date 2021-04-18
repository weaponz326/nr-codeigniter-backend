from rest_framework import serializers

from .models import Material


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = [
            'id', 
            'material_code',
            'material_name',
            'description',
            'category',
            'unit_price',
            'quantity',
        ]
