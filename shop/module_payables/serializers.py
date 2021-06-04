from rest_framework import serializers

from .models import Payable


class PayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payable
        fields = '__all__'
