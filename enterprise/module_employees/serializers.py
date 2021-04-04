from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id', 
            'first_name',
            'last_name',
            'sex',
            'date_of_birth',
            'photo',
            'nationality',
            'religion',
            'phone',
            'email',
            'address',
            'state',
            'city',
            'post_code',
            'employee_code',
            'department',
            'job',
            'pay_grade',
            'work_status',
            'started_work',
            'ended_work',
        ]

# merges first name and last name
class EmployeeListSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            'id', 
            'employee_name',
            'employee_code',
            'department',
        ]

    def get_employee_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
