from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Payment
from .serializers import PaymentSerializer, PaymentListSerializer, PaymentSumSerializer


# Create your views here.

class PaymentView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        payment = Payment.objects.filter(account=account)
        serializer = PaymentListSerializer(payment, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PaymentDetailView(APIView):
    def get(self, request, pk, format=None):
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSumSerializer(payment, context={'pk': pk})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        payment = Payment.objects.get(pk=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PaymentsHistoryView(APIView):
    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        payment = Payment.objects.filter(bill=bill)
        serializer = PaymentSerializer(payment, many=True)        
        return Response(serializer.data)

