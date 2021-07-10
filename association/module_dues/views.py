from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Dues, DuesPayment
from module_members.models import Member
from .serializers import DuesSerializer, DuesPaymentSerializer, DuesPaymentListSerializer


# Create your views here.

class DuesView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        dues = Dues.objects.filter(account=account)
        serializer = DuesSerializer(dues, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DuesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DuesDetailView(APIView):
    def get(self, request, pk, format=None):
        dues = Dues.objects.get(pk=pk)
        serializer = DuesSerializer(dues)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dues = Dues.objects.get(pk=pk)
        serializer = DuesSerializer(dues, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        dues = Dues.objects.get(pk=pk)
        dues.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# dues payment

class DuesPaymentView(APIView):
    def get(self, request, format=None):
        dues = self.request.query_params.get('dues', None)
        payment = DuesPayment.objects.filter(dues=dues)
        serializer = DuesPaymentListSerializer(payment, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DuesPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DuesPaymentDetailView(APIView):
    def get(self, request, pk, format=None):
        payment = DuesPayment.objects.get(pk=pk)
        serializer = DuesPaymentListSerializer(payment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payment = DuesPayment.objects.get(pk=pk)
        serializer = DuesPaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        payment = DuesPayment.objects.get(pk=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
