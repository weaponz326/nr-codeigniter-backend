from rest_framework import serializers

from .models import Dues, DuesPayment
from module_members.serializers import MemberListSerializer


class DuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dues
        fields = '__all__'

class DuesPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dues
        fields = '__all__'

class DuesPaymentListSerializer(serializers.ModelSerializer):

    # contains serializer method field
    member = MemberListSerializer()

    class Meta:
        model = Dues
        fields = '__all__'
        depth = 1