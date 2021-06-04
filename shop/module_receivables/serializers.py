from rest_framework import serializers

from .models import Receivable


class ReceivableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receivable
        fields = '__all__'            