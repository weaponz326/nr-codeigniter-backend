from rest_framework import serializers

from .models import Sales


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['id', 'sales_code', 'sales_date', 'unit_price', 'quantity']
