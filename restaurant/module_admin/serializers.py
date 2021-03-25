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
            'bills_access', 
            'deliveries_access', 
            'menu_access', 
            'orders_access', 
            'payments_access', 
            'portal_access', 
            'reservations_access', 
            'settings_access', 
            'sittings_access', 
            'staff_access', 
            'stock_access', 
            'tables_access', 
        ]

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'time', 'activity_module', 'description']
