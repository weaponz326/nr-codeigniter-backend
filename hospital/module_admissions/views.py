from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Admission
from .serializers import AdmissionSerializer, AdmissionListSerializer


# Create your views here.

class AdmissionView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        admission = Admission.objects.filter(account=account)
        serializer = AdmissionListSerializer(admission, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AdmissionDetailView(APIView):
    def get(self, request, pk, format=None):
        admission = Admission.objects.get(pk=pk)
        serializer = AdmissionListSerializer(admission)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        admission = Admission.objects.get(pk=pk)
        serializer = AdmissionSerializer(admission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        admission = Admission.objects.get(pk=pk)
        admission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
