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
            'portal_access', 
            'settings_access', 
        ]

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'time', 'activity_module', 'description']
