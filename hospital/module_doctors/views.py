from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Doctor
from accounts.models import Profile
from .serializers import DoctorSerializer, DoctorListSerializer


# Create your views here.

class DoctorView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = DoctorSerializer
        queryset = Doctor.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            doctor = Doctor(
                hospital=Profile.objects.get(id=request.data.get("hospital_id")),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                sex=request.data.get("sex"),
                date_of_birth=request.data.get("date_of_birth"),
                nationality=request.data.get("nationality"),
                religion=request.data.get("religion"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
                state=request.data.get("state"),
                city=request.data.get("city"),
                post_code=request.data.get("post_code"),
                doctor_code=request.data.get("doctor_code"),
                department=request.data.get("department"),
                speciality=request.data.get("speciality"),
                work_status=request.data.get("work_status"),
                stated_work=request.data.get("started_work"),
                ended_work=request.data.get("ended_work"),
            )
            doctor.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorListSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class DoctorDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
