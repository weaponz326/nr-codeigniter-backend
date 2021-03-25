from rest_framework import serializers

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            'id', 
            'reservation_code', 
            'reservation_date', 
            'customer_name',
            'number_guests'
            'number_tables' 
            'arrival_date' 
            'reservation_status'
        ]
