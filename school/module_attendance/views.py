from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Attendance
from accounts.models import Profile
from module_terms.models import Term
from module_classes.models import Class
from .serializers import AttendanceSerializer, AttendanceListSerializer


# Create your views here.

class AttendanceView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AttendanceSerializer
        queryset = Attendance.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            attendance = Attendance(
                account=Profile.objects.get(id=request.data.get("school_id")),
                source=Class.objects.get(id=request.data.get("source")),
                attendance_code=request.data.get("attendance_code"),
                attendance_name=request.data.get("attendance_name"),
            )
            attendance.save()
            latest_attendance = Attendance.objects.latest("id")

            return Response({
                'status': True,
                'attendance_id': latest_attendance.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class AttendanceListView(generics.ListAPIView):
    serializer_class = AttendanceListSerializer

    def get_queryset(self):
        queryset = Attendance.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class AttendanceDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
