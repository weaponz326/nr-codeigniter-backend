from rest_framework import serializers

from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

# merges first name and last name
class MemberListSerializer(serializers.ModelSerializer):
    member_name = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'

    def get_member_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
