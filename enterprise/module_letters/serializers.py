from rest_framework import serializers

from .models import Received
from .models import Sent


class ReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Received
        fields = '__all__'

class SentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sent
        fields = '__all__'
