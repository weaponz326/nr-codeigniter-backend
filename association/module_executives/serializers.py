from rest_framework import serializers

from .models import Executive
from module_members.serializers import MemberListSerializer


class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = '__all__'

class ExecutiveListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    member = MemberListSerializer()

    class Meta:
        model = Executive
        fields = '__all__'
