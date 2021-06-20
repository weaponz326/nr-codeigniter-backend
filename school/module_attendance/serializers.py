from rest_framework import serializers

from .models import Attendance, AttendanceSheet, AttendanceDays
from module_students.serializers import StudentListSerializer


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AttendanceSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class AttendanceSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceSheet
        fields = '__all__'

class AttendanceSheetListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    student = StudentListSerializer()

    class Meta:
        model = AttendanceSheet
        fields = '__all__'
        depth = 1

class AttendanceDaysSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceDays
        fields = '__all__'
