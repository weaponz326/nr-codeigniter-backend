from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer, EmployeeListSerializer


# Create your views here.

class EmployeeView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        employee = Employee.objects.filter(account=account)
        serializer = EmployeeListSerializer(employee, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class EmployeeDetailView(APIView):
    def get(self, request, pk, format=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeListSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
