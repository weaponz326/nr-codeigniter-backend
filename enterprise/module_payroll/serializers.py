from rest_framework import serializers
from .models import Payroll


class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = ['id', 'payroll_name', 'payroll_status', 'date_generated', 'month', 'year']
