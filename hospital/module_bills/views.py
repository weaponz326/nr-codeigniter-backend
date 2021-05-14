from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Bill, General
from .serializers import BillSerializer, BillListSerializer, GeneralSerializer


# Create your views here.

class BillView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        bill = Bill.objects.filter(account=account)
        serializer = BillListSerializer(bill, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class BillDetailView(APIView):
    def get(self, request, pk, format=None):
        bill = Bill.objects.get(pk=pk)
        serializer = BillListSerializer(bill)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bill = Bill.objects.get(pk=pk)
        serializer = BillSerializer(bill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        bill = Bill.objects.get(pk=pk)
        bill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# general items
# -------------------------------------------------------------------------------------------

class GeneralView(APIView):
    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        general = General.objects.filter(bill=bill)
        serializer = GeneralSerializer(general, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class GeneralDetailView(APIView):
    def get(self, request, pk, format=None):
        general = General.objects.get(pk=pk)
        serializer = GeneralSerializer(general)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        general = General.objects.get(pk=pk)
        serializer = GeneralSerializer(general, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        general = General.objects.get(pk=pk)
        general.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
