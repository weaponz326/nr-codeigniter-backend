from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Laboratory
from accounts.models import Profile
from module_patients.models import Patient
from module_doctors.models import Doctor
from .serializers import LaboratorySerializer, LaboratorySaveSerializer, PatientSerializer, DoctorSerializer


# Create your views here.

# create a new lab for the firat time with only the lab fields
class NewLaboratoryView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LaboratorySaveSerializer(data=request.data)
        if serializer.is_valid():
            lab = Laboratory(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                lab_code=request.data.get("lab_code"),
                lab_date=request.data.get("lab_date"),
                lab_type=request.data.get("lab_type"),
            )
            lab.save()
            latest_lab = Laboratory.objects.latest("id")

            return Response({
                'status': True,
                'lab_id': latest_lab.id
            })
        else:
            return Response({ 'status': False })

class LaboratoryView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = LaboratorySerializer
        queryset = Laboratory.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = LaboratorySaveSerializer(data=request.data)
        if serializer.is_valid():
            lab = Laboratory(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                patient=Patient.objects.get(id=request.data.get("patient_id")),
                doctor=Doctor.objects.get(id=request.data.get("doctor_id")),
                lab_code=request.data.get("lab_code"),
                lab_type=request.data.get("lab_type"),
                lab_date=request.data.get("lab_date"),
            )
            lab.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class LaboratoryListView(generics.ListAPIView):
    serializer_class = LaboratorySerializer

    def get_queryset(self):
        queryset = Laboratory.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class LaboratoryDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySaveSerializer

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
