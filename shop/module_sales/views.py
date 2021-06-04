from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Sales
from .serializers import SalesSerializer


# Create your views here.

class SalesView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        sales = Sales.objects.filter(account=account)
        serializer = SalesSerializer(sales, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class SalesDetailView(APIView):
    def get(self, request, pk, format=None):
        sales = Sales.objects.get(pk=pk)
        serializer = SalesSerializer(sales)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sales = Sales.objects.get(pk=pk)
        serializer = SalesSerializer(sales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        sales = Sales.objects.get(pk=pk)
        sales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
