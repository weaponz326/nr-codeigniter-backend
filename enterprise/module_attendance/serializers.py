from rest_framework import serializers

from .models import Attendance, AttendanceEmployee, AttendanceDay, AttendanceCheck
from module_employees.serializers import EmployeeListSerializer


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendanceEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceEmployee
        fields = '__all__'

class AttendanceEmployeeListSerializer(serializers.ModelSerializer):
    
    # contains serializer method field
    employee = EmployeeListSerializer()

    class Meta:
        model = AttendanceEmployee
        fields = '__all__'
        depth = 1

class AttendanceDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceDay
        fields = '__all__'

class AttendanceCheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceCheck
        fields = '__all__'
