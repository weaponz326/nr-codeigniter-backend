from rest_framework import serializers

from .models import Admission
from module_patients.serializers import PatientListSerializer


class AdmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admission
        fields = '__all__'

class AdmissionListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    patient = PatientListSerializer()

    class Meta:
        model = Admission
        fields = '__all__'
        depth = 1
