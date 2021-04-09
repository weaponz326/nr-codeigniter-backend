from rest_framework import serializers

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'location', 'rate', 'features', 'room_status']
