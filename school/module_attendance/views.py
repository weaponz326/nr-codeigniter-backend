from django.shortcuts import render
from datetime import date, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Attendance, AttendanceStudent, AttendanceDay, AttendanceCheck
from .serializers import (
    AttendanceSerializer, 
    AttendanceStudentSerializer, 
    AttendanceStudentListSerializer, 
    AttendanceDaySerializer,
    AttendanceCheckSerializer
)
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

        # fill students table
        student_list = []
        source = attendance_instance.source.id
        student_set = Student.objects.filter(clas=source)

        if student_set.exists():
            for student in student_set.iterator():
                this_student = AttendanceStudent.objects.filter(attendance=attendance, student=student.id)
                if not this_student.exists():
                    student_list.append(AttendanceStudent(attendance=attendance_instance, student=student))
            if not student_list == []: AttendanceStudent.objects.bulk_create(student_list)

        # fill days and checks
        add_day_list = []
        delete_day_list = []
        add_check_list = []        
        delete_check_list = []
        day_set = AttendanceDay.objects.filter(attendance=attendance)

        if day_set.exists():
            for new_day in daterange(from_date, to_date):
                for day in day_set.iterator():

                    if (new_day != day) and (new_day > to_date):
                        add_day_list.append(AttendanceDay(attendance=attendance_instance, day=str(new_day)))
                        if student_set.exists():
                            for student in student_set.iterator():
                                add_check_list.append(AttendanceCheck(attendance_student=student, day=str(new_day)))
                    
                    if (new_day != day) and (new_day < from_date):
                        delete_day_list.append({attendance:attendance_instance, day:day})
                        if student_set.exists():
                            for student in student_set.iterator():
                                delete_check_list.append({'attendance_student':student, 'day':day})

            if not add_day_list == []: AttendanceDay.objects.bulk_create(add_day_list)
            if not delete_day_list == []: AttendanceDay.objects.filter(attendance__in=delete_day_list[attendance], day__in=delete_day_list[day])
            if not add_check_list == []: AttendanceCheck.objects.bulk_create(add_check_list)
            if not delete_check_list == []: AttendanceCheck.objects.filter(attendance_student__in=delete_check_list[attendance], day__in=delete_day_list[day])
        
        else:
            for new_day in daterange(from_date, to_date):
                add_day_list.append(AttendanceDay(attendance=attendance_instance, day=str(new_day)))
                for student in student_set.iterator():
                    add_check_list.append(AttendanceCheck(attendance_student=student, day=str(new_day)))                    
            
            if not add_day_list == []: AttendanceDay.objects.bulk_create(add_day_list)
            if not add_check_list == []: AttendanceCheck.objects.bulk_create(add_check_list)
                    
        return Response({ 'message' : 'OK' })

class AttendanceDayView(APIView):
    def get(self, request, format=None):
        attendance = self.request.query_params.get('attendance', None)
        day = AttendanceDay.objects.filter(attendance=attendance)
        serializer = AttendanceDaySerializer(day, many=True)        
        return Response(serializer.data)

class AttendanceStudentView(APIView):
    def get(self, request, format=None):
        attendance = self.request.query_params.get('attendance', None)
        day = AttendanceStudent.objects.filter(attendance=attendance)
        serializer = AttendanceStudentListSerializer(day, many=True)        
        return Response(serializer.data)

class AttendanceCheckView(APIView):
    def get(self, request, format=None):
        attendance = self.request.query_params.get('attendance', None)
        check = AttendanceCheck.objects.filter(attendance_student__attendance=attendance)
        serializer = AttendanceCheckSerializer(check, many=True)        
        return Response(serializer.data)

class AttendanceCheckDetailView(APIView):
    def get(self, request, pk, format=None):
        attendance = AttendanceCheck.objects.get(pk=pk)
        serializer = AttendanceCheckSerializer(attendance)
        return Response(serializer.data)
