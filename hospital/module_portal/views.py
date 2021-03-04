from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import filters

from .models import Rink
from accounts.models import Profile
from module_admissions.models import Admission
from module_patients.models import Patient
from module_doctors.models import Doctor
from module_nurses.models import Nurse
from .serializers import RinkSerializer, ProfileSerializer, RinkDetailSerializer
from module_admissions.serializers import AdmissionSerializer
from module_patients.serializers import PatientSerializer
from module_doctors.serializers import DoctorSerializer
from module_nurses.serializers import NurseSerializer


# Create your views here.

class RinkView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = RinkSerializer
        queryset = Rink.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = RinkSerializer(data=request.data)
        if serializer.is_valid():
            rink = Rink(
                sender=Profile.objects.get(id=request.data.get("sender")),
                recipient=Profile.objects.get(id=request.data.get("recipient")),
                rink_type=request.data.get("rink_type"),
                rink_source=request.data.get("rink_source"),
                comment=request.data.get("comment")
            )
            rink.save()
            latest_rink = Rink.objects.latest("id")

            return Response({ 
                'status': True ,
                'rink_id': latest_rink.id
            })
        else:
            return Response({ 'status': False })

class SearchListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
class SearchDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# rink type sources

class AdmissionListView(generics.ListAPIView):
    serializer_class = AdmissionSerializer

    def get_queryset(self):
        queryset = Admission.objects.all()
        hospital = self.request.query_params.get('hospital', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        hospital = self.request.query_params.get('hospital', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()
        hospital = self.request.query_params.get('hospital', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class NurseListView(generics.ListAPIView):
    serializer_class = NurseSerializer

    def get_queryset(self):
        queryset = Nurse.objects.all()
        hospital = self.request.query_params.get('hospital', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset


# list all rinks of a user
class RinkListView(generics.ListAPIView):
    serializer_class = RinkDetailSerializer

    def get_queryset(self):
        queryset = Rink.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            # queryset = queryset.filter(recipient__id=user).filter(sender__id=user)
            queryset = queryset.filter(recipient__id=user)
        return queryset

# get a specific rink
class RinkDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Rink.objects.all()
    serializer_class = RinkDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# get single dource for rink details

class AdmissionDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class PatientDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class DoctorDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class NurseDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
