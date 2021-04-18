from rest_framework import serializers

from .models import Purchasing, PurchasingItem


class PurchasingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchasing
        fields = ['id', 'schedule_code', 'schedule_name', 'from_date', 'to_date']
