from rest_framework import serializers

from .models import Diagnosis
from module_patients.models import Patient
from module_doctors.models import Doctor


# patient and doctor to be merged into diagnosis serializer

class PatientSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'patient_name', 'clinical_number']

    def get_patient_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

class DoctorSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'doctor_name', 'doctor_code']

    def get_doctor_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

class DiagnosisSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = Diagnosis
        fields = [
            'id', 
            'account',
            'patient', 
            'doctor', 
            'diagnosis_code', 
            'diagnosis_date',
            'blood_group', 
            'temperature',
            'weight',
            'height',
            'blood_pressure',
            'pulse',
            'diagnosis_detail',
            'treatment',
            'remarks'
        ]

class DiagnosisSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagnosis
        fields = [
            'id',
            'diagnosis_code', 
            'diagnosis_date',
            'blood_group', 
            'temperature',
            'weight',
            'height',
            'blood_pressure',
            'pulse',
            'diagnosis_detail',
            'treatment',
            'remarks'
        ]

