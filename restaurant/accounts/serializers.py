from rest_framework import serializers
from .models import Profile
from module_admin.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# merge admin module user with restaurant profiles
class UserAccountsSerializer(serializers.ModelSerializer):
    account = ProfileSerializer()

    class Meta:
        model = User
        fields = ['account', 'personal_id']
