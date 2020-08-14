from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Appointment
        fields = ['id', 'user', 'subject', 'location', 'start', 'end', 'description', 'status']
