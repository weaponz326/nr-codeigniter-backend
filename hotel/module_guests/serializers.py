from rest_framework import serializers

from .models import Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'guest_code', 'first_name', 'last_name', 'sex', 'phone', 'email', 'address']
