from rest_framework import serializers

from .models import Prescription, Detail
from module_patients.models import Patient
from module_doctors.models import Doctor


# patient and doctor to be merged into prescription serializer

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

class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = Prescription
        fields = ['id', 'hospital', 'patient', 'doctor', 'prescription_code', 'prescription_date']

# for saving prescription patient and doctor with ids
# to prevent saving with dictionary        
class PrescriptionSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = ['id', 'hospital', 'patient', 'doctor', 'prescription_code', 'prescription_date']

# prescription details

class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detail
        fields = ['id', 'prescription', 'medicine', 'dosage', 'remarks']