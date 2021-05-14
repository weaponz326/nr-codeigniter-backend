from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer


# Create your views here.

class PatientView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        patient = Patient.objects.filter(account=account)
        serializer = PatientListSerializer(patient, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PatientDetailView(APIView):
    def get(self, request, pk, format=None):
        patient = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        patient = Patient.objects.get(pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
