from rest_framework import serializers

from .models import Ward, WardPatient
from module_patients.serializers import PatientListSerializer


class WardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ward
        fields = '__all__'

class WardPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardPatient
        fields = '__all__'

class WardPatientListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    patient = PatientListSerializer()

    class Meta:
        model = WardPatient
        fields = '__all__'
        depth = 1
