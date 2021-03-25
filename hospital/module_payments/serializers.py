from rest_framework import serializers

from .models import Payment
from module_patients.models import Patient
from module_admissions.models import Admission
from module_bills.models import Bill


# patient and admission to be merged into bill serializer

class PatientSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'patient_name', 'clinical_number']

    def get_patient_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

class AdmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admission
        fields = ['id', 'admission_code', 'admission_date']

class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ['id', 'bill_code', 'bill_date', 'total_amount']

class PaymentSerializer(serializers.ModelSerializer):
    bill = BillSerializer()

    class Meta:
        model = Payment
        fields = [
            'id', 
            'bill',
            'payment_code', 
            'payment_date', 
            'amount_paid', 
            'balance'
        ]

# for saving payment patient, admission and bill with ids
# to prevent saving with dictionary        
class PaymentSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            'id', 
            'bill', 
            'payment_code', 
            'payment_date', 
            'amount_paid', 
            'balance'
        ]