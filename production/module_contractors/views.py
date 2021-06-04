from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Contractor
from .serializers import ContractorSerializer


# Create your views here.

class ContractorView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        contractor = Contractor.objects.filter(account=account)
        serializer = ContractorSerializer(contractor, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContractorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ContractorDetailView(APIView):
    def get(self, request, pk, format=None):
        contractor = Contractor.objects.get(pk=pk)
        serializer = ContractorSerializer(contractor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contractor = Contractor.objects.get(pk=pk)
        serializer = ContractorSerializer(contractor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        contractor = Contractor.objects.get(pk=pk)
        contractor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
