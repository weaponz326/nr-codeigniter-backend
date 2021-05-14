from rest_framework import serializers

from .models import Procurement


class ProcurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurement
        fields = '__all__'
