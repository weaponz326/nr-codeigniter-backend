from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Patient
from accounts.models import Profile
from .serializers import PatientSerializer, PatientListSerializer


# Create your views here.

class PatientView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = PatientSerializer
        queryset = Patient.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            patient = Patient(
                hospital=Profile.objects.get(id=request.data.get("hospital_id")),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                sex=request.data.get("sex"),
                date_of_birth=request.data.get("date_of_birth"),
                nationality=request.data.get("nationality"),
                religion=request.data.get("religion"),
                occupation=request.data.get("occupation"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
                state=request.data.get("state"),
                city=request.data.get("city"),
                post_code=request.data.get("post_code"),
                clinical_number=request.data.get("clinical_number"),
                insurance_type=request.data.get("insurance_type"),
                insurance_number=request.data.get("insurance_number"),
            )
            patient.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class PatientListView(generics.ListAPIView):
    serializer_class = PatientListSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class PatientDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
