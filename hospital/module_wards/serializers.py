from rest_framework import serializers

from .models import Ward, WardPatient
from module_patients.models import Patient


class WardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ward
        fields = ['id', 'ward_number', 'ward_name', 'ward_type', 'location', 'capacity']

# ward's patients

# patient to be merged into ward's patient serializer

class PatientSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'patient_name', 'clinical_number']

    def get_patient_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

class WardPatientSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = WardPatient
        fields = ['id', 'ward', 'patient', 'bed_number', 'date_admitted', 'date_discharged', 'status']

# for saving ward's patient with ids
# to prevent saving with dictionary        
class WardPatientSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = WardPatient
        fields = ['id', 'ward', 'patient', 'bed_number', 'date_admitted', 'date_discharged', 'status']
