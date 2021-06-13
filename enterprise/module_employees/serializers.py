from rest_framework import serializers
from drf_base64.fields import Base64FileField

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)


    class Meta:
        model = Employee
        fields = '__all__'

# merges first name and last name
class EmployeeListSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    employee_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1

    def get_employee_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
