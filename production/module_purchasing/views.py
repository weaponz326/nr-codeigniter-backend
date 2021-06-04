from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Purchasing, PurchasingItem
from .serializers import PurchasingSerializer, PurchasingItemSerializer


# Create your views here.

class PurchasingView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        purchasing = Purchasing.objects.filter(account=account)
        serializer = PurchasingSerializer(purchasing, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchasingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PurchasingDetailView(APIView):
    def get(self, request, pk, format=None):
        purchasing = Purchasing.objects.get(pk=pk)
        serializer = PurchasingSerializer(purchasing)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        purchasing = Purchasing.objects.get(pk=pk)
        serializer = PurchasingSerializer(purchasing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        purchasing = Purchasing.objects.get(pk=pk)
        purchasing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------
# purhasing items

class PurchasingItemView(APIView):
    def get(self, request, format=None):
        purchasing = self.request.query_params.get('purchasing', None)
        item = PurchasingItem.objects.filter(purchasing=purchasing)
        serializer = PurchasingItemSerializer(item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchasingItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PurchasingItemDetailView(APIView):
    def get(self, request, pk, format=None):
        item = PurchasingItem.objects.get(pk=pk)
        serializer = PurchasingItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = PurchasingItem.objects.get(pk=pk)
        serializer = PurchasingItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = PurchasingItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
