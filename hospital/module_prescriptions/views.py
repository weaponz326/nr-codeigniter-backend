from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Prescription, Detail
from accounts.models import Profile
from module_patients.models import Patient
from module_doctors.models import Doctor
from .serializers import (
    PrescriptionSerializer, 
    PrescriptionSaveSerializer, 
    DetailSerializer, 
    PatientSerializer, 
    DoctorSerializer
)


# Create your views here.

# create a new prescription for the first time
class NewPrescriptionView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PrescriptionSaveSerializer(data=request.data)
        if serializer.is_valid():
            prescription = Prescription(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                prescription_code=request.data.get("prescription_code"),
                prescription_date=request.data.get("prescription_date"),
            )
            prescription.save()
            latest_prescription = Prescription.objects.latest("id")

            return Response({
                'status': True,
                'prescription_id': latest_prescription.id
            })
        else:
            return Response({ 'status': False })

class PrescriptionView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = PrescriptionSerializer
        queryset = Prescription.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = PrescriptionSaveSerializer(data=request.data)
        if serializer.is_valid():
            prescription = Prescription(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                patient=Patient.objects.get(id=request.data.get("patient_id")),
                doctor=Doctor.objects.get(id=request.data.get("doctor_id")),
                prescription_code=request.data.get("prescription_code"),
                prescription_date=request.data.get("prescription_date"),
            )
            prescription.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class PrescriptionListView(generics.ListAPIView):
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        queryset = Prescription.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class PrescriptionDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# prescription details
# ----------------------------------------------------------------------------------------------------------

class DetailView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = DetailSerializer
        queryset = Detail.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = DetailSerializer(data=request.data)
        if serializer.is_valid():
            detail = Detail(
                prescription=Prescription.objects.get(id=request.data.get("prescription_id")),
                medicine=request.data.get("medicine"),
                dosage=request.data.get("dosage"),
                remarks=request.data.get("remarks")
            )
            detail.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class DetailListView(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        queryset = Detail.objects.all()
        prescription = self.request.query_params.get('prescription', None)
        if prescription is not None:
            queryset = queryset.filter(prescription=prescription)
        return queryset

class DetailDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# patient and doctor select grid list
# --------------------------------------------------------------------------------------------------

class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset
