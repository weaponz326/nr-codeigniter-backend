from rest_framework import serializers
from drf_base64.fields import Base64FileField

from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    
    class Meta:
        model = Member
        fields = '__all__'

# merges first name and last name
class MemberListSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    member_name = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'

    def get_member_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
