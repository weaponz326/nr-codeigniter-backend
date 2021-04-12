from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'payment_code', 'payment_date', 'customer_name', 'amount_paid', 'balance']
