from rest_framework import serializers

from .models import Manufacturing


class ManufacturingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturing
        fields = '__all__'
