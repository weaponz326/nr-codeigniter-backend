from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Attendance, AttendanceMember, AttendanceDay, AttendanceCheck
from .serializers import (
    AttendanceSerializer, 
    AttendanceMemberSerializer, 
    AttendanceMemberListSerializer, 
    AttendanceDaySerializer,
    AttendanceCheckSerializer
)
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
                if not AttendanceMember.objects.filter(attendance=attendance, member=member.id).exists():
                    attendance_sheet_list.append(AttendanceMember(attendance=attendance_instance, member=member))                    
        AttendanceMember.objects.bulk_create(attendance_sheet_list)

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

            add_check_list = []        
            member_set = AttendanceMember.objects.filter(attendance=serializer.data.attendance)

            if member_set.exists():
                for member in member_set.iterator():
                    add_check_list.append(AttendanceCheck(attendance_member=member, day=str(serializer.data.day)))                                 
            if not add_check_list == []: AttendanceCheck.objects.bulk_create(add_check_list)
            return Response({ 'message': 'OK', 'data': serializer.data })
        
        return Response(serializer.errors)

class AttendanceMemberView(APIView):
    def get(self, request, format=None):
        attendance = self.request.query_params.get('attendance', None)
        day = AttendanceMember.objects.filter(attendance=attendance)
        serializer = AttendanceMemberListSerializer(day, many=True)        
        return Response(serializer.data)

class AttendanceCheckView(APIView):
    def get(self, request, format=None):
        attendance = self.request.query_params.get('attendance', None)
        check = AttendanceCheck.objects.filter(attendance_member__attendance=attendance)
        serializer = AttendanceCheckSerializer(check, many=True)        
        return Response(serializer.data)

class AttendanceCheckDetailView(APIView):
    def get(self, request, pk, format=None):
        attendance = AttendanceCheck.objects.get(pk=pk)
        serializer = AttendanceCheckSerializer(attendance)
        return Response(serializer.data)
