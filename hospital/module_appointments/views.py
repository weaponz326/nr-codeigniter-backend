from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Appointment
from .serializers import AppointmentSerializer, AppointmentListSerializer


# Create your views here.

class AppointmentView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        appointment = Appointment.objects.filter(account=account)
        serializer = AppointmentListSerializer(appointment, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AppointmentDetailView(APIView):
    def get(self, request, pk, format=None):
        appointment = Appointment.objects.get(pk=pk)
        serializer = AppointmentListSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        appointment = Appointment.objects.get(pk=pk)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        appointment = Appointment.objects.get(pk=pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
