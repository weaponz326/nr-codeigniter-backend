from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ExtendedProfile
from accounts.models import Profile


# merged profile and user
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'location', 'about']

class ExtendedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedProfile
        fields = [
            'id', 
            'country', 
            'state', 
            'city', 
            'phone1', 
            'phone2', 
            'email', 
            'address'
        ]

