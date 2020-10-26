from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Rink
from users.models import Profile

class RinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rink
        fields = ['id', 'sender', 'recipient', 'rink_date', 'rink_type', 'rink_source', 'comment']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer() 

    class Meta:
        model = Profile
        fields = ['id', 'user', 'location', 'about']

# gets all rinks with user profile merged to sender and recipient fields
class RinkDetailSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer()
    recipient = ProfileSerializer()

    class Meta:
        model = Rink
        fields = ['id', 'sender', 'recipient', 'rink_date', 'rink_type', 'rink_source', 'comment']
