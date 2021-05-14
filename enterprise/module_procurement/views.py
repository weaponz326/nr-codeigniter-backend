from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Procurement
from .serializers import ProcurementSerializer


# Create your views here.

class ProcurementView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        procurement = Procurement.objects.filter(account=account)
        serializer = ProcurementSerializer(procurement, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProcurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ProcurementDetailView(APIView):
    def get(self, request, pk, format=None):
        procurement = Procurement.objects.get(pk=pk)
        serializer = ProcurementSerializer(procurement)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        procurement = Procurement.objects.get(pk=pk)
        serializer = ProcurementSerializer(procurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        procurement = Procurement.objects.get(pk=pk)
        procurement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
