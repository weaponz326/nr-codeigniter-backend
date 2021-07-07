from rest_framework import serializers

from .models import Fee, FeesItem, ArrearsItem, TargetClass, Bill
from module_students.serializers import StudentListSerializer


class FeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fee
        fields = '__all__'

class TargetClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = TargetClass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TargetClassSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class FeesItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeesItem
        fields = '__all__'

class FeesItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeesItem
        fields = '__all__'

class ArrearsItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArrearsItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ArrearsItemSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class BillSerializer(serializers.ModelSerializer):

    # contains serializer menthod field
    student = StudentListSerializer()
    class Meta:
        model = Bill
        fields = '__all__'
        depth = 2
