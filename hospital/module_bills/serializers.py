from rest_framework import serializers

from .models import Bill, General
from module_patients.models import Patient
from module_admissions.models import Admission


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
    patient = PatientSerializer()
    admission = AdmissionSerializer()

    class Meta:
        model = Bill
        fields = ['id', 'patient', 'admission', 'bill_code', 'bill_date', 'total_amount']

# for saving
# to prevent saving with dictionary        
class BillSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ['id', 'bill_code', 'bill_date', 'total_amount']

# bill general items

class GeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = General
        fields = ['id', 'bill', 'item', 'amount']