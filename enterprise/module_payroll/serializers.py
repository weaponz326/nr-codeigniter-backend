from rest_framework import serializers
from .models import Payroll, PayrollSheet
from module_employees.serializers import EmployeeListSerializer

class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'

class PayrollSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollSheet
        fields = '__all__'

class PayrollSheetListSerializer(serializers.ModelSerializer):

    # contains serializer methodfield
    employee = EmployeeListSerializer()
    class Meta:
        model = PayrollSheet
        fields = '__all__'
        depth = 1
