from rest_framework import serializers

from .models import Ledger, LedgerItem


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'

class LedgerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerItem
        fields = '__all__'
