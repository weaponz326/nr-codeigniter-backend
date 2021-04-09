from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'booking_code', 'booking_date', 'guest_name', 'expected_arrival', 'booking_status']
