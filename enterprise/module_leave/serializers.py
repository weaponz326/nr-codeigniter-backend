from rest_framework import serializers

from .models import Leave
from module_employees.serializers import EmployeeListSerializer


class LeaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leave
        fields = '__all__'

class LeaveListSerializer(serializers.ModelSerializer):
    # contain serializer menthod fields
    employee = EmployeeListSerializer()

    class Meta:
        model = Leave
        fields = '__all__'
