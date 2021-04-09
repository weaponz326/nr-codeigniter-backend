from rest_framework import serializers

from .models import Service, ServiceItem


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_code', 'service_type', 'service_date']

class ServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        fields = ['id', 'item_date', 'amount']
