from rest_framework import serializers

from .models import Manufacturing


class ManufacturingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturing
        fields = [
            'id', 
            'manufacturing_code', 
            'description', 
            'start_date', 
            'end_date', 
            'quantity',
            'manufacturing_status',
            'remarks'
        ]
