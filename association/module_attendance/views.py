from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Attendance, AttendanceSheet, AttendanceDay
from .serializers import AttendanceSerializer, AttendanceSheetSerializer, AttendanceSheetListSerializer, AttendanceDaySerializer
from module_members.models import Member


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

# sheet
# ----------------------------------------------------------------------------------------------------------

class RefreshSheetView(APIView):
    def get(self, request, format=None):        
        attendance = self.request.query_params.get('attendance', None)
        attendance_instance = Attendance.objects.get(id=attendance)
                    
        # fill sheet table
        member_set = Member.objects.filter(account=attendance_instance.account)
        attendance_sheet_list = []

        if member_set.exists():
            for member in member_set.iterator():
                if not AttendanceSheet.objects.filter(attendance=attendance, member=member.id).exists():
                    attendance_sheet_list.append(AttendanceSheet(attendance=attendance_instance, member=member, checks={}))                    
        AttendanceSheet.objects.bulk_create(attendance_sheet_list)

        return Response({ 'message' : 'OK' })

class AttendanceDayView(APIView):
    def get(self, request, format=None):
        attendance = self.request.query_params.get('attendance', None)
        day = AttendanceDay.objects.filter(attendance=attendance)
        serializer = AttendanceDaySerializer(day, many=True)    
        return Response({ 'message' : 'OK', 'data' : serializer.data })

    def post(self, request, format=None):
        serializer = AttendanceDaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AttendanceSheetView(APIView):
    def get(self, request, format=None):
        attendance = self.request.query_params.get('attendance', None)
        sheet = AttendanceSheet.objects.filter(attendance=attendance)
        serializer = AttendanceSheetListSerializer(sheet, many=True)    
        return Response({ 'message' : 'OK', 'data': serializer.data })
