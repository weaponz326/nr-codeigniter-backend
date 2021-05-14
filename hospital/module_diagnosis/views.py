from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Diagnosis
from .serializers import DiagnosisSerializer, DiagnosisListSerializer


# Create your views here.

class DiagnosisView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        diagnosis = Diagnosis.objects.filter(account=account)
        serializer = DiagnosisListSerializer(diagnosis, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiagnosisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DiagnosisDetailView(APIView):
    def get(self, request, pk, format=None):
        diagnosis = Diagnosis.objects.get(pk=pk)
        serializer = DiagnosisListSerializer(diagnosis)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        diagnosis = Diagnosis.objects.get(pk=pk)
        serializer = DiagnosisSerializer(diagnosis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        diagnosis = Diagnosis.objects.get(pk=pk)
        diagnosis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
