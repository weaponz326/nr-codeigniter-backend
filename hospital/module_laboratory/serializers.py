from rest_framework import serializers

from .models import Laboratory
from module_patients.models import Patient
from module_doctors.models import Doctor


# patient and doctor to be merged into laboratory serializer

class PatientSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'hospital', 'patient_name', 'clinical_number']

    def get_patient_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

class DoctorSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'hospital', 'doctor_name', 'doctor_code']

    def get_doctor_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

class LaboratorySerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = Laboratory
        fields = ['id', 'hospital', 'patient', 'doctor', 'lab_code', 'lab_date', 'lab_type']

# for saving laboratory patient and doctor with ids
# to prevent saving with dictionary        
class LaboratorySaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Laboratory
        fields = ['id', 'hospital', 'patient', 'doctor', 'lab_code', 'lab_date', 'lab_type']