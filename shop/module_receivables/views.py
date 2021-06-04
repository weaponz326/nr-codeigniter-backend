from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Receivable
from .serializers import ReceivableSerializer


# Create your views here.

class ReceivableView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        receivable = Receivable.objects.filter(account=account)
        serializer = ReceivableSerializer(receivable, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceivableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ReceivableDetailView(APIView):
    def get(self, request, pk, format=None):
        receivable = Receivable.objects.get(pk=pk)
        serializer = ReceivableSerializer(receivable)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        receivable = Receivable.objects.get(pk=pk)
        serializer = ReceivableSerializer(receivable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        receivable = Receivable.objects.get(pk=pk)
        receivable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
