from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Staff
from .serializers import StaffSerializer, StaffListSerializer


# Create your views here.

class StaffView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        staff = Staff.objects.filter(account=account)
        serializer = StaffListSerializer(staff, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class StaffDetailView(APIView):
    def get(self, request, pk, format=None):
        staff = Staff.objects.get(pk=pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        staff = Staff.objects.get(pk=pk)
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
