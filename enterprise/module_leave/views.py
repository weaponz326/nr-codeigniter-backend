from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Leave
from .serializers import LeaveSerializer, LeaveListSerializer


# Create your views here.

class LeaveView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        leave = Leave.objects.filter(account=account)
        serializer = LeaveListSerializer(leave, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class LeaveDetailView(APIView):
    def get(self, request, pk, format=None):
        leave = Leave.objects.get(pk=pk)
        serializer = LeaveListSerializer(leave)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        leave = Leave.objects.get(pk=pk)
        serializer = LeaveSerializer(leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        leave = Leave.objects.get(pk=pk)
        leave.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
