from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer


# Create your views here.

class AccountView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        account = Account.objects.filter(user=user)
        serializer = AccountSerializer(account, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AccountDetailView(APIView):
    def get(self, request, pk, format=None):
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        account = Account.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------------
# transactions

class TransactionView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        transaction = Transaction.objects.filter(account=account)
        serializer = TransactionSerializer(transaction, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class TransactionDetailView(APIView):
    def get(self, request, pk, format=None):
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        transaction = Transaction.objects.get(pk=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# all transactions
class AllTransactionsView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        account = Transaction.objects.filter(account__user=user)
        serializer = TransactionSerializer(account, many=True)        
        return Response(serializer.data)
