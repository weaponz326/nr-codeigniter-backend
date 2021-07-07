from django.db.models import Sum
from rest_framework import serializers

from .models import Payment
from module_fees.serializers import BillSerializer

class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentListSerializer(serializers.ModelSerializer):

    # contains serilizer method field
    bill = BillSerializer()
    class Meta:
        model = Payment
        fields = '__all__'
        depth: 2

class PaymentSumSerializer(serializers.ModelSerializer):

    # contains serilaizer method field
    bill = BillSerializer()
    amount_paid = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'  
        depth = 2     

    def get_amount_paid(self, obj):
        pk = self.context.get('pk')
        payment = Payment.objects.get(pk=pk)
        bill = payment.bill
        return Payment.objects.filter(bill=bill.id).aggregate(Sum('payment')) 
