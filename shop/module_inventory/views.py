from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import InventoryItem
from .serializers import InventoryItemSerializer


# Create your views here.

class InventoryItemView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        item = InventoryItem.objects.filter(account=account)
        serializer = InventoryItemSerializer(item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class InventoryItemDetailView(APIView):
    def get(self, request, pk, format=None):
        item = InventoryItem.objects.get(pk=pk)
        serializer = InventoryItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = InventoryItem.objects.get(pk=pk)
        serializer = InventoryItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = InventoryItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
