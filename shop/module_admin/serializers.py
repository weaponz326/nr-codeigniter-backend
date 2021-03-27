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
            'cashflow_access', 
            'customers_access', 
            'inventory_access', 
            'invoice_access', 
            'marketting_access', 
            'orders_access', 
            'payments_access', 
            'payables_access', 
            'portal_access', 
            'products_access', 
            'purcahsing_access', 
            'receivables_access', 
            'sales_access', 
            'settings_access', 
            'staff_access', 
        ]

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'time', 'activity_module', 'description']
