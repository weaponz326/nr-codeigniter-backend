from rest_framework import serializers

from .models import Roster


class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roster
        fields = '__all__'
