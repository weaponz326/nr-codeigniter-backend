from django.shortcuts import render
from datetime import date, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Attendance, AttendanceSheet, AttendanceDay
from .serializers import AttendanceSerializer, AttendanceSheetSerializer, AttendanceSheetListSerializer, AttendanceDaySerializer
from module_employees.models import Employee


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
        
        def daterange(from_date, to_date):
            for n in range(int((to_date - from_date).days)):
                yield from_date + timedelta(n)

        # to be used in filling both days and sheet tables
        attendance = self.request.query_params.get('attendance', None)
        attendance_instance = Attendance.objects.get(id=attendance)
        
    	# fill days table        
        from_date = attendance_instance.from_date
        to_date = attendance_instance.to_date

        add_list = []
        delete_list = []
        day_set = AttendanceDay.objects.filter(attendance=attendance)

        # new_day = day in date range of days between from_date and to_date from attendance model
        # day = day from attendace_day model 

        if day_set.exists():
            for new_day in daterange(from_date, to_date):
                for day in day_set.iterator():
                    if (new_day != day) and (new_day > to_date):
                        add_list.append(AttendanceDay(attendance=attendance_instance, day=new_day))
                    if (new_day != day) and (new_day < from_date):
                        delete_list.append({attendance:attendance_instance, day:day})

            if not add_list == []: AttendanceDay.objects.bulk_create(add_list)
            if not delete_list == []: AttendanceDay.objects.filter(attendance__in=delete_list[attendance], day__in=delete_list[day])
        else:
            for new_day in daterange(from_date, to_date):
                add_list.append(AttendanceDay(attendance=attendance_instance, day=new_day))
            if not add_list == []: AttendanceDay.objects.bulk_create(add_list)
            
        # fill sheet table
        employee_set = Employee.objects.filter(account=attendance_instance.account)
        attendance_sheet_list = []

        if employee_set.exists():
            for employee in employee_set.iterator():
                if not AttendanceSheet.objects.filter(attendance=attendance, employee=employee.id).exists():
                    # TODO: cannot add employee to filter
                    attendance_sheet_list.append(AttendanceSheet(attendance=attendance_instance, employee=employee, checks={}))                    
        AttendanceSheet.objects.bulk_create(attendance_sheet_list)

        return Response({ 'message' : 'OK' })

class AttendanceConfigView(APIView):
    def get(self, request, format=None):
        attendance = self.request.query_params.get('attendance', None)
        day = AttendanceDay.objects.filter(attendance=attendance)
        serializer = AttendanceDaySerializer(day, many=True)    
        return Response({ 'message' : 'OK', 'data' : serializer.data })

class AttendanceSheetView(APIView):
    def get(self, request, format=None):
        attendance = self.request.query_params.get('attendance', None)
        sheet = AttendanceSheet.objects.filter(attendance=attendance)
        serializer = AttendanceSheetListSerializer(sheet)    
        return Response({ 'message' : 'OK', 'data': serializer.data })
