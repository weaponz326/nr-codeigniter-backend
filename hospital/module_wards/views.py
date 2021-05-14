from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Ward, WardPatient
from .serializers import WardSerializer, WardPatientSerializer, WardPatientListSerializer


# Create your views here.

class WardView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        ward = Ward.objects.filter(account=account)
        serializer = WardSerializer(ward, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class WardDetailView(APIView):
    def get(self, request, pk, format=None):
        ward = Ward.objects.get(pk=pk)
        serializer = WardSerializer(ward)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ward = Ward.objects.get(pk=pk)
        serializer = WardSerializer(ward, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        ward = Ward.objects.get(pk=pk)
        ward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------
# ward's patients

class WardPatientView(APIView):
    def get(self, request, format=None):
        ward = self.request.query_params.get('ward', None)
        patient = WardPatient.objects.filter(ward=ward)
        serializer = WardPatientListSerializer(patient, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WardPatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class WardPatientDetailView(APIView):
    def get(self, request, pk, format=None):
        patient = WardPatient.objects.get(pk=pk)
        serializer = WardPatientListSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = WardPatient.objects.get(pk=pk)
        serializer = WardPatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        patient = WardPatient.objects.get(pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
