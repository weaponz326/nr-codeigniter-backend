from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import MenuItem
from .serializers import MenuItemSerializer


# Create your views here.

class MenuItemView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        item = MenuItem.objects.filter(account=account)
        serializer = MenuItemSerializer(item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class MenuItemDetailView(APIView):
    def get(self, request, pk, format=None):
        item = MenuItem.objects.get(pk=pk)
        serializer = MenuItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = MenuItem.objects.get(pk=pk)
        serializer = MenuItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = MenuItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
