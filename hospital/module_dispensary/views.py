from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Dispensary, Detail
from accounts.models import Profile
from module_prescriptions.models import Prescription
from .serializers import (
    DispensarySerializer, 
    DispensarySaveSerializer, 
    DetailSerializer, 
    DetailSaveSerializer, 
    PrescriptionSerializer
)

# Create your views here.

# create a new dispensary for the first time
class NewDispensaryView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DispensarySaveSerializer(data=request.data)
        if serializer.is_valid():
            dispensary = Dispensary(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                dispense_code=request.data.get("dispense_code"),
                dispense_date=request.data.get("dispense_date"),
            )
            dispensary.save()
            latest_dispensary = Dispensary.objects.latest("id")

            return Response({
                'status': True,
                'dispensary_id': latest_dispensary.id
            })
        else:
            return Response({ 'status': False })

class DispensaryView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = DispensarySerializer
        queryset = Dispensary.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = DispensarySaveSerializer(data=request.data)
        if serializer.is_valid():
            dispensary = Dispensary(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                prescription=Prescripton.objects.get(id=request.data.get("prescription_id")),
                dispensary_code=request.data.get("dispensary_code"),
                dispensary_date=request.data.get("dispensary_date"),
            )
            dispensary.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class DispensaryListView(generics.ListAPIView):
    serializer_class = DispensarySerializer

    def get_queryset(self):
        queryset = Dispensary.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class DispensaryDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Dispensary.objects.all()
    serializer_class = DispensarySaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# dispensary details
# ----------------------------------------------------------------------------------------------------------

class DetailView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = DetailSerializer
        queryset = Detail.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = DetailSaveSerializer(data=request.data)
        if serializer.is_valid():
            detail = Detail(
                dispensary=Dispensary.objects.get(id=request.data.get("dispensary_id")),
                drug=request.data.get("drug"),
                remarks=request.data.get("remarks")
            )
            drug.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class DetailListView(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        queryset = Drug.objects.all()
        dispensary = self.request.query_params.get('dispensary', None)
        if dispensary is not None:
            queryset = queryset.filter(dispensary=dispensary)
        return queryset

class DetailDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Detail.objects.all()
    serializer_class = DetailSaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# prescription select grid list
# --------------------------------------------------------------------------------------------------

class PrescriptionListView(generics.ListAPIView):
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        queryset = Prescription.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

