from rest_framework import serializers

from .models import Appointment
from module_patients.serializers import PatientListSerializer
from module_doctors.serializers import DoctorListSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        
class AppointmentListSerializer(serializers.ModelSerializer):
    # contains serializer method fields
    patient = PatientListSerializer()
    consultant = DoctorListSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'
        depth = 1