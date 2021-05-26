from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Executive
from .serializers import ExecutiveSerializer, ExecutiveListSerializer


# Create your views here.

class ExecutiveView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        executive = Executive.objects.filter(account=account)
        serializer = ExecutiveListSerializer(executive, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExecutiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ExecutiveDetailView(APIView):
    def get(self, request, pk, format=None):
        executive = Executive.objects.get(pk=pk)
        serializer = ExecutiveListSerializer(executive)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        executive = Executive.objects.get(pk=pk)
        serializer = ExecutiveSerializer(executive, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        executive = Executive.objects.get(pk=pk)
        executive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
