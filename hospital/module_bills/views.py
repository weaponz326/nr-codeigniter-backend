from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Bill, 
    General,
    AppointmentCharge,
    LaboratoryCharge,
    DispensaryCharge,
    WardCharge
)
from .serializers import (
    BillSerializer, 
    BillListSerializer, 
    GeneralSerializer,
    AppointmentChargeSerializer,
    LaboratoryChargeSerializer,
    DispensaryChargeSerializer,
    WardChargeSerializer
)


# Create your views here.

class BillView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        bill = Bill.objects.filter(account=account)
        serializer = BillListSerializer(bill, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class BillDetailView(APIView):
    def get(self, request, pk, format=None):
        bill = Bill.objects.get(pk=pk)
        serializer = BillListSerializer(bill)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bill = Bill.objects.get(pk=pk)
        serializer = BillSerializer(bill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        bill = Bill.objects.get(pk=pk)
        bill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# general items
# -------------------------------------------------------------------------------------------

class GeneralView(APIView):
    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        general = General.objects.filter(bill=bill)
        serializer = GeneralSerializer(general, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class GeneralDetailView(APIView):
    def get(self, request, pk, format=None):
        general = General.objects.get(pk=pk)
        serializer = GeneralSerializer(general)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        general = General.objects.get(pk=pk)
        serializer = GeneralSerializer(general, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        general = General.objects.get(pk=pk)
        general.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# extra charges items
# -------------------------------------------------------------------------------------------

# appointment charges

class AppointmentChargeView(APIView):
    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        appointment = AppointmentCharge.objects.filter(bill=bill)
        serializer = AppointmentChargeSerializer(appointment, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppointmentChargeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AppointmentChargeDetailView(APIView):
    def get(self, request, pk, format=None):
        appointment = AppointmentCharge.objects.get(pk=pk)
        serializer = AppointmentChargeSerializer(appointment)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        appointment = AppointmentCharge.objects.get(pk=pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# dispensary charges

class DispensaryChargeView(APIView):
    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        dispensary = DispensaryCharge.objects.filter(bill=bill)
        serializer = DispensaryChargeSerializer(dispensary, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DispensaryChargeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DispensaryChargeDetailView(APIView):
    def get(self, request, pk, format=None):
        dispensary = DispensaryCharge.objects.get(pk=pk)
        serializer = DispensaryChargeSerializer(dispensary)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        dispensary = DispensaryCharge.objects.get(pk=pk)
        dispensary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# laboratory charges

class LaboratoryChargeView(APIView):
    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        laboratory = LaboratoryCharge.objects.filter(bill=bill)
        serializer = LaboratoryChargeSerializer(laboratory, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LaboratoryChargeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class LaboratoryChargeDetailView(APIView):
    def get(self, request, pk, format=None):
        laboratory = LaboratoryCharge.objects.get(pk=pk)
        serializer = LaboratoryChargeSerializer(laboratory)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        laboratory = LaboratoryCharge.objects.get(pk=pk)
        laboratory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ward charges

class WardChargeView(APIView):
    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        ward = WardCharge.objects.filter(bill=bill)
        serializer = WardChargeSerializer(ward, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WardChargeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class WardChargeDetailView(APIView):
    def get(self, request, pk, format=None):
        ward = WardCharge.objects.get(pk=pk)
        serializer = WardChargeSerializer(ward)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        ward = WardCharge.objects.get(pk=pk)
        ward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
