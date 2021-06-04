from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Payable
from .serializers import PayableSerializer


# Create your views here.

class PayableView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        payable = Payable.objects.filter(account=account)
        serializer = PayableSerializer(payable, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PayableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PayableDetailView(APIView):
    def get(self, request, pk, format=None):
        payable = Payable.objects.get(pk=pk)
        serializer = PayableSerializer(payable)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payable = Payable.objects.get(pk=pk)
        serializer = PayableSerializer(payable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        payable = Payable.objects.get(pk=pk)
        payable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
