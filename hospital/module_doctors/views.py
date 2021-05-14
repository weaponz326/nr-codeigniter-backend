from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Doctor
from accounts.models import Profile
from .serializers import DoctorSerializer, DoctorListSerializer


# Create your views here.

class DoctorView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        doctor = Doctor.objects.filter(account=account)
        serializer = DoctorListSerializer(doctor, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DoctorDetailView(APIView):
    def get(self, request, pk, format=None):
        doctor = Doctor.objects.get(pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        doctor = Doctor.objects.get(pk=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        doctor = Doctor.objects.get(pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
