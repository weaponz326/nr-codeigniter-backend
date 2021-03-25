from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Ward, WardPatient
from accounts.models import Profile
from module_patients.models import Patient
from .serializers import (
    WardSerializer, 
    WardPatientSerializer, 
    WardPatientSaveSerializer, 
    PatientSerializer, 
)


# Create your views here.

class WardView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = WardSerializer
        queryset = Ward.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = WardSerializer(data=request.data)
        if serializer.is_valid():
            ward = Ward(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                ward_number=request.data.get("ward_number"),
                ward_name=request.data.get("ward_name"),
                ward_type=request.data.get("ward_type"),
                location=request.data.get("location"),
                capacity=request.data.get("capacity"),
            )
            ward.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class WardListView(generics.ListAPIView):
    serializer_class = WardSerializer

    def get_queryset(self):
        queryset = Ward.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class WardDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Ward.objects.all()
    serializer_class = WardSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------------------
# ward's patients

# for listing ward's patients
class WardPatientListView(generics.ListAPIView):
    serializer_class = WardPatientSerializer

    def get_queryset(self):
        queryset = WardPatient.objects.all()
        ward = self.request.query_params.get('ward', None)
        if ward is not None:
            queryset = queryset.filter(ward=ward)
        return queryset

# for creating new ward's patient
class WardPatientSaveView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = WardPatientSaveSerializer(data=request.data)
        if serializer.is_valid():
            patient = WardPatient(
                ward=Ward.objects.get(id=request.data.get("ward_id")),
                patient=Ward.objects.get(id=request.data.get("patient_id")),
                bed_number=request.data.get("bed_number"),
                date_admitted=request.data.get("date_admitted"),
                date_discharged=request.data.get("date_discharged"),
                status=request.data.get("status")
            )
            patient.save()
            latest_ward = Ward.objects.latest("id")

            return Response({
                'status': True,
                'ward_id': latest_ward.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class WardPatientDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = WardPatient.objects.all()
    serializer_class = WardPatientSaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# patient select grid list
# --------------------------------------------------------------------------------------------------

class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset
