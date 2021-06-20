from rest_framework import serializers

from .models import Attendance, AttendanceDay, AttendanceSheet
from module_members.serializers import MemberListSerializer


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
    member = MemberListSerializer()

    class Meta:
        model = AttendanceSheet
        fields = '__all__'

class AttendanceDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceDay
        fields = '__all__'
