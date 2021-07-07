from rest_framework import serializers

from .models import (
    Roster,
    RosterSheet, 
    Shift, 
    Batch, 
    RosterDay,
    DoctorsPersonnel,
    NursesPersonnel,
    StaffPersonnel
)
from module_doctors.serializers import DoctorListSerializer
from module_nurses.serializers import NurseListSerializer
from module_staff.serializers import StaffListSerializer

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

class RosterDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterDay
        fields = '__all__'

class RosterSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterSheet
        fields = '__all__'
        depth = 1
                                
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

class NursesPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NursesPersonnel
        fields = '__all__'

class NursesPersonnelListSerializer(serializers.ModelSerializer):
    # contain serializer menthod fields
    nurse = NurseListSerializer()

    class Meta:
        model = NursesPersonnel
        fields = '__all__'
        depth = 1

class StaffPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPersonnel
        fields = '__all__'

class StaffPersonnelListSerializer(serializers.ModelSerializer):
    # contain serializer menthod fields
    staff = StaffListSerializer()

    class Meta:
        model = StaffPersonnel
        fields = '__all__'
        depth = 1
