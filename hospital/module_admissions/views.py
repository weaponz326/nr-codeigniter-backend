from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Admission
from accounts.models import Profile
from module_patients.models import Patient
from .serializers import AdmissionSerializer, AdmissionSaveSerializer, PatientSerializer


# Create your views here.

class AdmissionView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AdmissionSerializer
        queryset = Admission.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = AdmissionSaveSerializer(data=request.data)
        if serializer.is_valid():
            admission = Admission(
                hospital=Profile.objects.get(id=request.data.get("hospital_id")),
                patient=Patient.objects.get(id=request.data.get("patient_id")),
                admission_code=request.data.get("admission_code"),
                admission_date=request.data.get("admission_date"),
                discharge_date=request.data.get("discharge_date"),
                admission_status=request.data.get("admission_status"),
            )
            admission.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class AdmissionListView(generics.ListAPIView):
    serializer_class = AdmissionSerializer

    def get_queryset(self):
        queryset = Admission.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class AdmissionDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Admission.objects.all()
    serializer_class = AdmissionSaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# patient select grid list

class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset
