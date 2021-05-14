from rest_framework import serializers

from .models import Fee, FeesItem

class FeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fee
        fields = '__all__'

class FeesItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeesItem
        fields = '__all__'
