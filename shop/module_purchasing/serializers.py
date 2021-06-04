from rest_framework import serializers

from .models import Purchasing, PurchasingItem


class PurchasingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchasing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PurchasingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
class PurchasingItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchasing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PurchasingItemSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1