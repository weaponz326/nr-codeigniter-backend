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
            'admin_access', 
            'contractors_access', 
            'equipment_access', 
            'manufacturing_access', 
            'orders_access', 
            'portal_access', 
            'products_access', 
            'projects_access', 
            'purchasing_access', 
            'schedule_access', 
            'settings_access', 
            'stock_access', 
            'tasks_access', 
            'workers_access', 
        ]

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'time', 'activity_module', 'description']
