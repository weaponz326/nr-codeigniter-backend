from rest_framework import serializers

from .models import ExtendedProfile


class ExtendedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedProfile
        fields = '__all__'