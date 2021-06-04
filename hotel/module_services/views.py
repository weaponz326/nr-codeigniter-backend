from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Service, ServiceItem
from .serializers import ServiceSerializer, ServiceItemSerializer


# Create your views here.

class ServiceView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        service = Service.objects.filter(account=account)
        serializer = ServiceSerializer(service, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ServiceDetailView(APIView):
    def get(self, request, pk, format=None):
        service = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        service = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        service = Service.objects.get(pk=pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------------------------------------
# service item

class ServiceItemView(APIView):
    def get(self, request, format=None):
        service = self.request.query_params.get('service', None)
        item = ServiceItem.objects.filter(service=service)
        serializer = ServiceItemSerializer(item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ServiceItemDetailView(APIView):
    def get(self, request, pk, format=None):
        item = ServiceItem.objects.get(pk=pk)
        serializer = ServiceItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = ServiceItem.objects.get(pk=pk)
        serializer = ServiceItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = ServiceItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
