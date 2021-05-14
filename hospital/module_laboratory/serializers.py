from rest_framework import serializers

from .models import Laboratory, Attachment
from module_patients.serializers import PatientListSerializer
from module_doctors.serializers import DoctorListSerializer


# patient and doctor to be merged into laboratory serializer

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'

class LaboratoryListSerializer(serializers.ModelSerializer):
    # contain serializer method field
    patient = PatientListSerializer()
    doctor = DoctorListSerializer()

    class Meta:
        model = Laboratory
        fields = '__all__'
        depth = 1

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
