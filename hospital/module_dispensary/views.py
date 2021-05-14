from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Dispensary, DispensaryDrug
from .serializers import DispensarySerializer, DispensaryListSerializer, DispensaryDrugSerializer

# Create your views here.

class DispensaryView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        dispensary = Dispensary.objects.filter(account=account)
        serializer = DispensaryListSerializer(dispensary, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DispensarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DispensaryDetailView(APIView):
    def get(self, request, pk, format=None):
        dispensary = Dispensary.objects.get(pk=pk)
        serializer = DispensaryListSerializer(dispensary)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dispensary = Dispensary.objects.get(pk=pk)
        serializer = DispensarySerializer(dispensary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        dispensary = Dispensary.objects.get(pk=pk)
        dispensary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# dispensary drugs
# -----------------------------------------------------------------------------------------------------------

class DispensaryDrugView(APIView):
    def get(self, request, format=None):
        dispensary = self.request.query_params.get('dispensary', None)
        drug = DispensaryDrug.objects.filter(dispensary=dispensary)
        serializer = DispensaryDrugSerializer(drug, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DispensaryDrugSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DispensaryDrugDetailView(APIView):
    def get(self, request, pk, format=None):
        drug = DispensaryDrug.objects.get(pk=pk)
        serializer = DispensaryDrugSerializer(drug)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        drug = DispensaryDrug.objects.get(pk=pk)
        serializer = DispensaryDrugSerializer(drug, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        drug = DispensaryDrug.objects.get(pk=pk)
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
