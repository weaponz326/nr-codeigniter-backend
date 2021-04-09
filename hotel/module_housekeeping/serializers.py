from rest_framework import serializers

from .models import Housekeeping, Checklist


class HousekeepingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housekeeping
        fields = ['id', 'housekeeping_code', 'housekeeping_code']

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = ['id', 'item_number', 'item_description', 'status', 'remarks']
