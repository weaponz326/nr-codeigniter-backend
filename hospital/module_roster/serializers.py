from rest_framework import serializers

from .models import Roster, Shift, Batch, DoctorsPersonnel
from module_doctors.serializers import DoctorListSerializer

class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roster
        fields = '__all__'
        
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
                        
class DoctorsPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsPersonnel
        fields = '__all__'

class DoctorsPersonnelListSerializer(serializers.ModelSerializer):
    # contain serializer menthod fields
    doctor = DoctorListSerializer()

    class Meta:
        model = DoctorsPersonnel
        fields = '__all__'
        depth = 1

