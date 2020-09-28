from django.contrib.auth.models import User

from rest_framework import serializers

from users.models import Profile
# from .models import 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer() 

    class Meta:
        model = Profile
        # fields = ['user', 'location', 'about']

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['location', 'about', 'description']

# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()
    
#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'profile']

