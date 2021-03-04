from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ExtendedProfile
from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

# merged profile and user
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'location', 'about']

class ExtendedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedProfile
        fields = [
            'id', 
            'user', 
            'gender', 
            'date_of_birth', 
            'country', 
            'state', 
            'city', 
            'phone', 
            'email', 
            'address'
        ]

