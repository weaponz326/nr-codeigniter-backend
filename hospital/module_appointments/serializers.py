from rest_framework import serializers

from .models import Appointment
from module_patients.models import Patient
from module_doctors.models import Doctor


# patient and doctor to be merged into appoitment serializer

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

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    consultant = DoctorSerializer()

    class Meta:
        model = Appointment
        fields = [
            'id', 
            'hospital', 
            'patient', 
            'consultant', 
            'appointment_code', 
            'appointment_for', 
            'remarks', 
            'appointment_status'
        ]

# for saving appointment patient and consultant with ids
# to prevent saving with dictionary        
class AppointmentSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = [
            'id', 
            'hospital', 
            'patient', 
            'consultant', 
            'appointment_code', 
            'appointment_for', 
            'remarks', 
            'appointment_status'
        ]