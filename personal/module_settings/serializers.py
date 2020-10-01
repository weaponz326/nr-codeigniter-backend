from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class SettingsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'profile', 'date_of_birth', 'gender', 'photo']
