from rest_framework import serializers

from .models import Sitting


class SittingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitting
        fields = '__all__'