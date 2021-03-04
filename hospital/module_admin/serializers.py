from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['hospital', 'personal_id', 'is_admin', 'is_manager', 'is_creator']

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user', 
            'admin_access', 
            'admissions_access', 
            'appointments_access', 
            'bills_access', 
            'diagnosis_access', 
            'dispensary_access', 
            'doctors_access', 
            'drugs_access', 
            'laboratory_access', 
            'nurses_access', 
            'patients_access', 
            'payments_access', 
            'portal_access', 
            'prescriptions_access', 
            'settings_access', 
            'staff_access', 
            'wards_access'            
        ]

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'time', 'activity_module', 'description']
