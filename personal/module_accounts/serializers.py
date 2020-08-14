from rest_framework import serializers
from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user', 'account_name', 'account_number', 'bank_name']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'transaction_date', 'description', 'transaction_type', 'amount']

# to be merged with transactions
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user']

# merged with user serializer to get user
class UserTransactionSerializer(serializers.ModelSerializer):
    account = UserSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'description', 'transaction_date', 'transaction_type', 'amount']