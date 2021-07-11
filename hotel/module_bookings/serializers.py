from rest_framework import serializers

from .models import Booking, BookedRoom


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

class BookedRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookedRoom
        fields = '__all__'
