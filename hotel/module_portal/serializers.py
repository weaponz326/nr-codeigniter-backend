from rest_framework import serializers

from .models import Rink
from accounts.models import Profile

class RinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rink
        fields = ['id', 'sender', 'recipient', 'rink_date', 'rink_type', 'rink_source', 'comment']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'location', 'about']

# gets all rinks with user profile merged to sender and recipient fields
class RinkDetailSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer()
    recipient = ProfileSerializer()

    class Meta:
        model = Rink
        fields = ['id', 'sender', 'recipient', 'rink_date', 'rink_type', 'rink_source', 'comment']
