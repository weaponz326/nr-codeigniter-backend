from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ExtendedProfile
from accounts.models import Profile


class ExtendedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedProfile
        fields = '__all__'
        