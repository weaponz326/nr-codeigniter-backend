from rest_framework import serializers

from .models import Dispensary, Detail
from module_prescriptions.models import Prescription
from module_patients.models import Patient
from module_doctors.models import Doctor
from module_drugs.models import Drug


# patient and doctor to be merged into prescription
# then prescription will be merged with dispensary serializer

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

# merge prescription containing patient and doctor to dispensary
class DispensarySerializer(serializers.ModelSerializer):
    prescription = PrescriptionSerializer()

    class Meta:
        model = Dispensary
        fields = ['id', 'hospital', 'prescription', 'dispense_code', 'dispense_date']

# for saving dispensary's prescription with id
# to prevent saving with dictionary        
class DispensarySaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = ['id', 'hospital', 'prescription', 'dispense_code', 'dispense_date']

# -----------------------------------------------------------------------------------------------------------
# dispensary details

# merge drug into dispensary detail serializer

class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drug
        fields = ['id', 'ndc_number', 'drug_name']

class DetailSerializer(serializers.ModelSerializer):
    drug = DrugSerializer()

    class Meta:
        model = Detail
        fields = ['id', 'dispensary', 'drug', 'remarks']

# for saving dispensary's detail drug with id
# to prevent saving with dictionary        
class DetailSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detail
        fields = ['id', 'dispensary', 'drug', 'remarks']
