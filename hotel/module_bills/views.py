from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Bill
from .serializers import BillSerializer


# Create your views here.

class BillView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        bill = Bill.objects.filter(account=account)
        serializer = BillSerializer(bill, many=True)        
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
        serializer = BillSerializer(bill)
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
