from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Diagnosis
from accounts.models import Profile
from module_patients.models import Patient
from module_doctors.models import Doctor
from .serializers import DiagnosisSerializer, DiagnosisSaveSerializer, PatientSerializer, DoctorSerializer


# Create your views here.

# create a new diagnosis for the first time 
class NewDiagnosisView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DiagnosisSaveSerializer(data=request.data)
        if serializer.is_valid():
            diagnosis = Diagnosis(
                hospital=Profile.objects.get(id=request.data.get("hospital_id")),
                diagnosis_code=request.data.get("diagnosis_code"),
                diagnosis_date=request.data.get("diagnosis_date"),
            )
            diagnosis.save()
            ladetail_diagnosis = Diagnosis.objects.ladetail("id")

            return Response({
                'status': True,
                'diagnosis_id': ladetail_diagnosis.id
            })
        else:
            return Response({ 'status': False })

class DiagnosisView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = DiagnosisSerializer
        queryset = Diagnosis.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = DiagnosisSaveSerializer(data=request.data)
        if serializer.is_valid():
            diagnosis = Diagnosis(
                hospital=Profile.objects.get(id=request.data.get("hospital_id")),
                patient=Patient.objects.get(id=request.data.get("patient_id")),
                doctor=Doctor.objects.get(id=request.data.get("doctor_id")),
                diagnosis_code=request.data.get("diagnosis_code"),
                diagnosis_date=request.data.get("diagnosis_date"),
                blood_group=request.data.get("detail_name"),
                temperature=request.data.get("temperature"),
                weight=request.data.get("weight"),
                height=request.data.get("height"),
                blood_pressure=request.data.get("blood_pressure"),
                pulse=request.data.get("pulse"),
                diagnosis_detail=request.data.get("diagnosis_detail"),
                treatment=request.data.get("treatment"),
                remarks=request.data.get("remarks")
            )
            diagnosis.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class DiagnosisListView(generics.ListAPIView):
    serializer_class = DiagnosisSerializer

    def get_queryset(self):
        queryset = Diagnosis.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class DiagnosisDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSaveSerializer

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
