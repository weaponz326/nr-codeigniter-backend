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
            'assets_access',             
            'bills_access',             
            'bookings_access',             
            'checkin_access',             
            'guests_access',             
            'housekeeping_access',             
            'payments_access',             
            'portal_access',             
            'rooms_access',             
            'services_access',             
            'settings_access',             
            'staff_access',             
        ]

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'time', 'activity_module', 'description']
