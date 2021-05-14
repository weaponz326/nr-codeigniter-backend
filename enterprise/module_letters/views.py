from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Received, Sent
from .serializers import ReceivedSerializer, SentSerializer


# Create your views here.

# received letters
# -------------------------------------------------------------------------------------------

class ReceivedView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        received = Received.objects.filter(account=account)
        serializer = ReceivedSerializer(received, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceivedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ReceivedDetailView(APIView):
    def get(self, request, pk, format=None):
        received = Received.objects.get(pk=pk)
        serializer = ReceivedSerializer(received)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        received = Received.objects.get(pk=pk)
        serializer = ReceivedSerializer(received, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        received = Received.objects.get(pk=pk)
        received.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# sent letters
# -------------------------------------------------------------------------------------------

class SentView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        sent = Sent.objects.filter(account=account)
        serializer = SentSerializer(sent, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class SentDetailView(APIView):
    def get(self, request, pk, format=None):
        sent = Sent.objects.get(pk=pk)
        serializer = SentSerializer(sent)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sent = Sent.objects.get(pk=pk)
        serializer = SentSerializer(sent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        sent = Sent.objects.get(pk=pk)
        sent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
