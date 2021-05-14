from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


# Create your views here.

class OrderView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        order = Order.objects.filter(account=account)
        serializer = OrderSerializer(order, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class OrderDetailView(APIView):
    def get(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# order item

class OrderItemView(APIView):
    def get(self, request, format=None):
        order = self.request.query_params.get('order', None)
        item = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class OrderItemDetailView(APIView):
    def get(self, request, pk, format=None):
        item = OrderItem.objects.get(pk=pk)
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = OrderItem.objects.get(pk=pk)
        serializer = OrderItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = OrderItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
