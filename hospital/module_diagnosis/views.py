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
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                diagnosis_code=request.data.get("diagnosis_code"),
                diagnosis_date=request.data.get("diagnosis_date"),
            )
            diagnosis.save()
            latest_diagnosis = Diagnosis.objects.latest("id")

            return Response({
                'status': True,
                'diagnosis_id': latest_diagnosis.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class DiagnosisListView(generics.ListAPIView):
    serializer_class = DiagnosisSerializer

    def get_queryset(self):
        queryset = Diagnosis.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class DiagnosisView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSaveSerializer

    def put(self, request, *args, kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class DiagnosisDetailView(generics.RetrieveAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

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
