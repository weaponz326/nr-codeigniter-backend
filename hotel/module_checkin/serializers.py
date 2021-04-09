from rest_framework import serializers

from .models import Checkin


class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = ['id', 'checkin_code', 'checkin_date', 'checkout_date', 'number_nights']
