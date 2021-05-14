from rest_framework import serializers

from .models import Prescription, PrescriptionDetail
from module_patients.serializers import PatientListSerializer
from module_doctors.serializers import DoctorListSerializer

class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = '__all__'

class PrescriptionListSerializer(serializers.ModelSerializer):
    # contain serializer menthod fields
    patient = PatientListSerializer()
    doctor = DoctorListSerializer()

    class Meta:
        model = Prescription
        fields = '__all__'
        depth = 1


# prescription details

class PrescriptionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrescriptionDetail
        fields = '__all__'