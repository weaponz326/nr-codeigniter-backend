from django.db.models import Sum
from rest_framework import serializers

from .models import Payment
from module_bills.serializers import BillListSerializer


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  

class PaymentListSerializer(serializers.ModelSerializer):
    # contains serilaizer method field
    bill = BillListSerializer()

    class Meta:
        model = Payment
        fields = '__all__'  
        depth = 2     

class PaymentSumSerializer(serializers.ModelSerializer):
    # contains serilaizer method field
    bill = BillListSerializer()
    amount_paid = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'  
        depth = 2     

    # TODO: not working
    def get_amount_paid(self, obj):
        pk = self.context.get('pk')
        payment = Payment.objects.get(id=pk)
        bill = payment.bill.id
        return Payment.objects.filter(bill__id=bill).aggregate(Sum('payment')) 
        # return Payment.objects.aggregate(Sum('payment'))         