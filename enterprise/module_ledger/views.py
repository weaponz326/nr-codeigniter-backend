from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Ledger, LedgerItem
from .serializers import LedgerSerializer, LedgerItemSerializer


# Create your views here.

# ledger

class LedgerView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        ledger = Ledger.objects.filter(account=account)
        serializer = LedgerSerializer(ledger, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LedgerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class LedgerDetailView(APIView):
    def get(self, request, pk, format=None):
        ledger = Ledger.objects.get(pk=pk)
        serializer = LedgerSerializer(ledger)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ledger = Ledger.objects.get(pk=pk)
        serializer = LedgerSerializer(ledger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        ledger = Ledger.objects.get(pk=pk)
        ledger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------------------
# ledger items

class LedgerItemView(APIView):
    def get(self, request, format=None):
        ledger = self.request.query_params.get('ledger', None)
        item = LedgerItem.objects.filter(ledger=ledger)
        serializer = LedgerItemSerializer(item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LedgerItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class LedgerItemDetailView(APIView):
    def get(self, request, pk, format=None):
        item = LedgerItem.objects.get(pk=pk)
        serializer = LedgerItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = LedgerItem.objects.get(pk=pk)
        serializer = LedgerItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = LedgerItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
