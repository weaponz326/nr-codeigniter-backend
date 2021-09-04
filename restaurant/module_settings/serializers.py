from rest_framework import serializers

from .models import ExtendedProfile, Subscription


class ExtendedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedProfile
        fields = '__all__'
        
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
                