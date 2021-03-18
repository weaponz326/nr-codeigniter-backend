from rest_framework import serializers

from .models import Attendance
from module_terms.models import Term
from module_classes.models import Class


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'attendance_code', 'attendance_name']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name', 'department']

# merge attendance and subjects
class AttendanceListSerializer(serializers.ModelSerializer):
    source = ClassSerializer()

    class Meta:
        model = Attendance
        fields = ['id', 'source', 'attendance_code', 'attendance_name']
