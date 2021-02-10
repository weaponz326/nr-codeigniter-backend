from rest_framework import serializers

from .models import Sitting


class SittingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitting
        fields = [
            'id', 
            'restaurant', 
            'sitting_code', 
            'sitting_date', 
            'arrival_time', 
            'departure_time', 
            'customer_name', 
            'number_guests'
        ]
