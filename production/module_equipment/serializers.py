from rest_framework import serializers

from .models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            'id', 
            'equipment_code', 
            'equipment_name', 
            'equipment_type', 
            'category', 
            'brand', 
            'model', 
            'serial_number', 
            'description', 
            'location', 
            'condition', 
            'equipment_status',
        ]
