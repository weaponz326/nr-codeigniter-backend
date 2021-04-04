from rest_framework import serializers

from .models import Received
from .models import Sent


class ReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Received
        fields = ['id', 'reference_number', 'letter_date', 'sender', 'subject', 'date_received']

class SentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sent
        fields = ['id', 'reference_number', 'letter_date', 'recipient', 'subject', 'date_sent']
