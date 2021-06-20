from django.shortcuts import render
from datetime import date, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Attendance, AttendanceSheet, AttendanceDays
from .serializers import AttendanceSerializer, AttendanceSheetSerializer, AttendanceSheetListSerializer, AttendanceDaysSerializer
from module_students.models import Student


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
            instance = serializer.save()

            # create attendance dyas after creating attendance
            days = AttendanceDays(days={})
            days.id = instance.id
            days.save()

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
        
        def daterange(from_date, to_date):
            for n in range(int((to_date - from_date).days)):
                yield from_date + timedelta(n)

        # to be used in filling both days and sheet tables
        attendance_id = self.request.query_params.get('attendance', None)
        attendance = Attendance.objects.get(id=attendance_id)
        
    	# fill days table        
        from_date = attendance.from_date
        to_date = attendance.to_date
        days = {};

        for day in daterange(from_date, to_date):
            days.update(day)

        attendance_days = AttendanceDays(days=days)
        attendance_days.attendance = attendance_id
        attendance_days.save()    

        # fill sheet table
        class_id = attendance.source.id
        students = Student.objects.filter(clas=class_id)

        for student in students:
            # TODO: cannot add student to filter
            if not AttendanceSheet.objects.get(attendance=attendance_id, student=student.id):
                sheet_item = AttendanceSheet(student=student.id)
                sheet_item.save()

        return Response({ 'message' : 'OK' })
