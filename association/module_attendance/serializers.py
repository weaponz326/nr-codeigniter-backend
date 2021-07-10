from rest_framework import serializers

from .models import Attendance, AttendanceDay, AttendanceMember, AttendanceCheck
from module_members.serializers import MemberListSerializer


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendanceMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceMember
        fields = '__all__'

class AttendanceMemberListSerializer(serializers.ModelSerializer):

    # contains serializer method field
    member = MemberListSerializer()

    class Meta:
        model = AttendanceMember
        fields = '__all__'

class AttendanceDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceDay
        fields = '__all__'

class AttendanceCheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceCheck
        fields = '__all__'
