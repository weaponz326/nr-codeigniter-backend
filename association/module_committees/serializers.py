from rest_framework import serializers

from .models import Committee, CommitteeMember
from module_members.serializers import MemberListSerializer


class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = '__all__'

class CommitteeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeMember
        fields = '__all__'

class CommitteeMemberListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    member = MemberListSerializer()

    class Meta:
        model = CommitteeMember
        fields = '__all__'
