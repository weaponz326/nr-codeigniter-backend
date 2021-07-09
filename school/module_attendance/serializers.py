from rest_framework import serializers

from .models import Attendance, AttendanceStudent, AttendanceDay, AttendanceCheck
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

class AttendanceStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceStudent
        fields = '__all__'

class AttendanceStudentListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    student = StudentListSerializer()

    class Meta:
        model = AttendanceStudent
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
