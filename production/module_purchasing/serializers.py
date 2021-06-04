from rest_framework import serializers

from .models import Purchasing, PurchasingItem


class PurchasingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchasing
        fields = '__all__'

class PurchasingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasingItem
        fields = '__all__'
