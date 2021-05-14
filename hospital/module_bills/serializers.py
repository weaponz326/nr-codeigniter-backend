from rest_framework import serializers

from .models import Bill, General
from module_patients.serializers import PatientListSerializer


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'

class BillListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    patient = PatientListSerializer()

    class Meta:
        model = Bill
        fields = '__all__'
        depth = 1

# bill general items

class GeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = General
        fields = '__all__'