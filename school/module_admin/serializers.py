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
            'admin_access', 
            'assessment_access', 
            'attendance_access', 
            'classes_access', 
            'fees_access', 
            'parents_access', 
            'payments_access', 
            'portal_access', 
            'reports_access', 
            'settings_access', 
            'staff_access', 
            'students_access', 
            'students_access', 
            'subjects_access', 
            'teachers_access', 
            'terms_access'
        ]

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'time', 'activity_module', 'description']
