from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Fee, FeesItem
from .serializers import FeeSerializer, FeesItemSerializer


# Create your views here.

class FeeView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        fee = Fee.objects.filter(account=account)
        serializer = FeeSerializer(fee, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class FeeDetailView(APIView):
    def get(self, request, pk, format=None):
        fee = Fee.objects.get(pk=pk)
        serializer = FeeSerializer(fee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fee = Fee.objects.get(pk=pk)
        serializer = FeeSerializer(fee, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        fee = Fee.objects.get(pk=pk)
        fee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------
# fees item

class FeesItemView(APIView):
    def get(self, request, format=None):
        fee = self.request.query_params.get('fee', None)
        item = FeesItem.objects.filter(fee=fee)
        serializer = FeesItemSerializer(item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeesItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class FeesItemDetailView(APIView):
    def get(self, request, pk, format=None):
        item = FeesItem.objects.get(pk=pk)
        serializer = FeesItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = FeesItem.objects.get(pk=pk)
        serializer = FeesItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = FeesItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
