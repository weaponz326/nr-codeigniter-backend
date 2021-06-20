from rest_framework import serializers

from .models import Attendance, AttendanceSheet, AttendanceDay
from module_employees.serializers import EmployeeListSerializer


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendanceSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceSheet
        fields = '__all__'

class AttendanceSheetListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    employee = EmployeeListSerializer()

    class Meta:
        model = AttendanceSheet
        fields = '__all__'
        depth = 1

class AttendanceDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceDay
        fields = '__all__'
