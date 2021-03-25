from rest_framework import serializers

from .models import Payment
from module_bills.models import Bill


# patient and admission to be merged into bill serializer

class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ['id', 'bill_code', 'bill_date']

class PaymentSerializer(serializers.ModelSerializer):
    bill = BillSerializer()

    class Meta:
        model = Payment
        fields = ['id', 'bill', 'payment_code', 'payment_date', 'amount_paid', 'balance']

# for saving payment bill with id
# to prevent saving with dictionary        
class PaymentSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['id', 'bill', 'payment_code', 'payment_date', 'amount_paid', 'balance']