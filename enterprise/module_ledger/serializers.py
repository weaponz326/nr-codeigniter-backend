from rest_framework import serializers

from .models import Ledger, LedgerItem


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['id', 'ledger_code', 'ledger_date', 'ledger_name', 'from_date', 'to_date']

class LedgerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerItem
        fields = ['id', 'item_date', 'details', 'item_type', 'amount', 'balance']
