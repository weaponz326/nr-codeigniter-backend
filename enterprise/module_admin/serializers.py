from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['account', 'personal_id', 'is_admin', 'is_manager', 'is_creator']

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user', 
            'accounts_access', 
            'admin_access', 
            'appraisal_access', 
            'assets_access', 
            'attendance_access', 
            'budget_access', 
            'employees_access', 
            'files_access', 
            'leave_access', 
            'ledger_access', 
            'letters_access', 
            'payroll_access', 
            'portal_access', 
            'procurement_access', 
            'reception_access', 
            'settings_access', 
        ]

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'time', 'activity_module', 'description']
