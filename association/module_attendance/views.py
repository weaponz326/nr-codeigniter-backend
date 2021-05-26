from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Attendance
from .serializers import AttendanceSerializer


# Create your views here.

class AttendanceView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        attendance = Attendance.objects.filter(account=account)
        serializer = AttendanceSerializer(attendance, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AttendanceDetailView(APIView):
    def get(self, request, pk, format=None):
        attendance = Attendance.objects.get(pk=pk)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        attendance = Attendance.objects.get(pk=pk)
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        attendance = Attendance.objects.get(pk=pk)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
