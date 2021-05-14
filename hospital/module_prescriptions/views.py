from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Prescription, PrescriptionDetail
from .serializers import PrescriptionSerializer, PrescriptionListSerializer, PrescriptionDetailSerializer


# Create your views here.

class PrescriptionView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        prescription = Prescription.objects.filter(account=account)
        serializer = PrescriptionListSerializer(prescription, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PrescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PrescriptionDetailView(APIView):
    def get(self, request, pk, format=None):
        prescription = Prescription.objects.get(pk=pk)
        serializer = PrescriptionListSerializer(prescription)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        prescription = Prescription.objects.get(pk=pk)
        serializer = PrescriptionSerializer(prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        prescription = Prescription.objects.get(pk=pk)
        prescription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# prescription details
# ----------------------------------------------------------------------------------------------------------

# removed Prescription from infront of class names
# to prevent class names from clashing

class DetailView(APIView):
    def get(self, request, format=None):
        prescription = self.request.query_params.get('prescription', None)
        detail = PrescriptionDetail.objects.filter(prescription=prescription)
        serializer = PrescriptionDetailSerializer(detail, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PrescriptionDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DetailDetailView(APIView):
    def get(self, request, pk, format=None):
        detail = PrescriptionDetail.objects.get(pk=pk)
        serializer = PrescriptionDetailSerializer(detail)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        detail = PrescriptionDetail.objects.get(pk=pk)
        serializer = PrescriptionDetailSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        detail = PrescriptionDetail.objects.get(pk=pk)
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
