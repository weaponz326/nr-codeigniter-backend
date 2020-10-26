from django.contrib.auth.models import User
from rest_framework import serializers

from .models import AdditionalProfile, LocationDetails, Contact
from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'location', 'about']

# merged profile and user
class ProfileUserSerializer(serializers.ModelSerializer):
    user = UserSerializer() 

    class Meta:
        model = Profile
        fields = ['id', 'user', 'location', 'about']

class AdditionalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalProfile
        fields = ['id', 'user', 'gender', 'date_of_birth']

class LocationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationDetails
        fields = ['id', 'user', 'country', 'state', 'city']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'user', 'backup_email', 'phone']