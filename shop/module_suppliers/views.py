from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Supplier, SupplierProduct
from .serializers import SupplierSerializer, SupplierProductSerializer


# Create your views here.

class SupplierView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        supplier = Supplier.objects.filter(account=account)
        serializer = SupplierSerializer(supplier, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class SupplierDetailView(APIView):
    def get(self, request, pk, format=None):
        supplier = Supplier.objects.get(pk=pk)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        supplier = Supplier.objects.get(pk=pk)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        supplier = Supplier.objects.get(pk=pk)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------
# supplier products

class SupplierProductView(APIView):
    def get(self, request, format=None):
        supplier = self.request.query_params.get('supplier', None)
        supplier_product = SupplierProduct.objects.filter(supplier=supplier)
        serializer = SupplierProductSerializer(supplier_product, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SupplierProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class SupplierProductDetailView(APIView):
    def get(self, request, pk, format=None):
        supplier_product = SupplierProduct.objects.get(pk=pk)
        serializer = SupplierProductSerializer(supplier_product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        supplier_product = SupplierProduct.objects.get(pk=pk)
        serializer = SupplierProductSerializer(supplier_product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        supplier_product = SupplierProduct.objects.get(pk=pk)
        supplier_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
