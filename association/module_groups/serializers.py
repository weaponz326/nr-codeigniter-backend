from rest_framework import serializers

from .models import Group, GroupMember
from module_members.serializers import MemberListSerializer


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = '__all__'

class GroupMemberListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    member = MemberListSerializer()

    class Meta:
        model = GroupMember
        fields = '__all__'
