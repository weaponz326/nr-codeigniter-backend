from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id', 
            'restaurant', 
            'first_name',
            'last_name',
            'sex',
            'phone',
            'email',
            'address',
            'state',
            'city',
            'post_code',
            'customer_code',
            'religion',
            'allergies',
            'preferences'
        ]

# merges first name and last name
class CustomerListSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = [
            'id', 
            'restaurant', 
            'customer_name',
            'sex',
            'phone',
            'customer_code'
        ]

    def get_customer_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
