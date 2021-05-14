from rest_framework import serializers

from .models import Diagnosis
from module_patients.serializers import PatientListSerializer
from module_doctors.serializers import DoctorListSerializer



class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'

class DiagnosisListSerializer(serializers.ModelSerializer):
    # contains serializer method fields
    patient = PatientListSerializer()
    doctor = DoctorListSerializer()

    class Meta:
        model = Diagnosis
        fields = '__all__'
        depth = 1