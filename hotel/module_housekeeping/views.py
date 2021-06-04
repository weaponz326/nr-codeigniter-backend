from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Housekeeping, Checklist
from .serializers import HousekeepingSerializer, ChecklistSerializer


# Create your views here.

class HousekeepingView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        housekeeping = Housekeeping.objects.filter(account=account)
        serializer = HousekeepingSerializer(housekeeping, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HousekeepingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class HousekeepingDetailView(APIView):
    def get(self, request, pk, format=None):
        housekeeping = Housekeeping.objects.get(pk=pk)
        serializer = HousekeepingSerializer(housekeeping)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        housekeeping = Housekeeping.objects.get(pk=pk)
        serializer = HousekeepingSerializer(housekeeping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        housekeeping = Housekeeping.objects.get(pk=pk)
        housekeeping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------
# checklist

class ChecklistView(APIView):
    def get(self, request, format=None):
        housekeeping = self.request.query_params.get('housekeeping', None)
        checklist = Checklist.objects.filter(housekeeping=housekeeping)
        serializer = ChecklistSerializer(checklist, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChecklistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ChecklistDetailView(APIView):
    def get(self, request, pk, format=None):
        checklist = Checklist.objects.get(pk=pk)
        serializer = ChecklistSerializer(checklist)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        checklist = Checklist.objects.get(pk=pk)
        serializer = ChecklistSerializer(checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        checklist = Checklist.objects.get(pk=pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
