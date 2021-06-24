from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Payroll
from .serializers import PayrollSerializer


# Create your views here.

class PayrollView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        payroll = Payroll.objects.filter(account=account)
        serializer = PayrollSerializer(payroll, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PayrollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PayrollDetailView(APIView):
    def get(self, request, pk, format=None):
        payroll = Payroll.objects.get(pk=pk)
        serializer = PayrollSerializer(payroll)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payroll = Payroll.objects.get(pk=pk)
        serializer = PayrollSerializer(payroll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        payroll = Payroll.objects.get(pk=pk)
        payroll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
