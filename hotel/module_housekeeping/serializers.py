from rest_framework import serializers

from .models import Housekeeping, Checklist


class HousekeepingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housekeeping
        fields = '__all__'

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = '__all__'
