from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Attendance
from accounts.models import Profile
from .serializers import AttendanceSerializer


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
                account=Profile.objects.get(id=request.data.get("enterprise_id")),
                attendance_code=request.data.get("attendance_code"),
                attendance_name=request.data.get("attendance_name"),
                year=request.data.get("year"),
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
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = Attendance.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
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
