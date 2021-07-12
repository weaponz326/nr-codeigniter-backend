from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer, InvoiceItemSerializer


# Create your views here.

class InvoiceView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        invoice = Invoice.objects.filter(account=account)
        serializer = InvoiceSerializer(invoice, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class InvoiceDetailView(APIView):
    def get(self, request, pk, format=None):
        invoice = Invoice.objects.get(pk=pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        invoice = Invoice.objects.get(pk=pk)
        serializer = InvoiceSerializer(invoice, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        invoice = Invoice.objects.get(pk=pk)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# invoice item

class InvoiceItemView(APIView):
    def get(self, request, format=None):
        invoice = self.request.query_params.get('invoice', None)
        item = InvoiceItem.objects.filter(invoice=invoice)
        serializer = InvoiceItemSerializer(item, many=True, context={'request': request})        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvoiceItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class InvoiceItemDetailView(APIView):
    def get(self, request, pk, format=None):
        item = InvoiceItem.objects.get(pk=pk)
        serializer = InvoiceItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = InvoiceItem.objects.get(pk=pk)
        serializer = InvoiceItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = InvoiceItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
