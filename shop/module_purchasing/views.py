from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Purchasing, PurchasingItem
from accounts.models import Profile
from .serializers import PurchasingSerializer


# Create your views here.

class PurchasingView(APIView):
    def get(self, request, format=None):
        supplier = self.request.query_params.get('supplier', None)
        purchasing = Purchasing.objects.filter(supplier=supplier)
        serializer = PurchasingSerializer(purchasing, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchasingSerializer(data=request.data, context={'request': request})
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
        serializer = PurchasingSerializer(purchasing, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        purchasing = Purchasing.objects.get(pk=pk)
        purchasing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------------------
# purchasing items

class PurchasingItemView(APIView):
    def get(self, request, format=None):
        supplier = self.request.query_params.get('supplier', None)
        purchasing_item = PurchasingItem.objects.filter(supplier=supplier)
        serializer = PurchasingItemSerializer(purchasing_item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchasingItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PurchasingItemDetailView(APIView):
    def get(self, request, pk, format=None):
        purchasing_item = PurchasingItem.objects.get(pk=pk)
        serializer = PurchasingItemSerializer(purchasing_item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        purchasing_item = PurchasingItem.objects.get(pk=pk)
        serializer = PurchasingItemSerializer(purchasing_item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        purchasing_item = PurchasingItem.objects.get(pk=pk)
        purchasing_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
