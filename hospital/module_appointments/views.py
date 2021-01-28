from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Appointment
from accounts.models import Profile
from module_patients.models import Patient
from module_doctors.models import Doctor
from .serializers import AppointmentSerializer, PatientSerializer, DoctorSerializer, AppointmentSaveSerializer


# Create your views here.

class AppointmentView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AppointmentSerializer
        queryset = Appointment.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = AppointmentSaveSerializer(data=request.data)
        if serializer.is_valid():
            appointment = Appointment(
                hospital=Profile.objects.get(id=request.data.get("hospital_id")),
                patient=Patient.objects.get(id=request.data.get("patient_id")),
                consultant=Doctor.objects.get(id=request.data.get("doctor_id")),
                appointment_date=request.data.get("appointment_date"),
                appointment_for=request.data.get("appointment_for"),
                remarks=request.data.get("remarks"),
                appointment_status=request.data.get("appointment_status")
            )
            appointment.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class AppointmentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# patient and doctor select grid list

class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset
