from rest_framework import serializers

from .models import Admission
from module_patients.models import Patient
from module_doctors.models import Doctor


# patient to be merged into admission serializer

class PatientSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'hospital', 'patient_name', 'clinical_number']

    def get_patient_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

class AdmissionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Admission
        fields = ['id', 'hospital', 'patient', 'admission_code', 'admission_date', 'discharge_date', 'admission_status']

# for saving admission patient ids
# to prevent saving with dictionary        
class AdmissionSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admission
        fields = ['id', 'hospital', 'patient', 'admission_code', 'admission_date', 'discharge_date', 'admission_status']
