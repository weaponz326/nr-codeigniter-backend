from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Bill, General
from accounts.models import Profile
from module_patients.models import Patient
from module_admissions.models import Admission
from .serializers import (
    BillSerializer, 
    BillSaveSerializer, 
    GeneralSerializer, 
    PatientSerializer, 
    AdmissionSerializer
)


# Create your views here.

# create a new bill for the first time
class NewBillView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BillSaveSerializer(data=request.data)
        if serializer.is_valid():
            bill = Bill(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                patient=Patient.objects.get(id=request.data.get("patient_id")),
                admission=Admission.objects.get(id=request.data.get("admission_id")),
                bill_code=request.data.get("bill_code"),
                bill_date=request.data.get("bill_date"),
                total_amount=request.data.get("total_amount"),
            )
            bill.save()
            latest_bill = Bill.objects.latest("id")

            return Response({
                'status': True,
                'bill_id': latest_bill.id
            })
        else:
            return Response({ 'status': False })

class BillView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = BillSerializer
        queryset = Bill.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = BillSaveSerializer(data=request.data)
        if serializer.is_valid():
            bill = Bill(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                patient=Patient.objects.get(id=request.data.get("patient_id")),
                admission=Admission.objects.get(id=request.data.get("admission_id")),
                bill_code=request.data.get("bill_code"),
                bill_date=request.data.get("bill_date"),
                total_amount=request.data.get("total_amount"),
            )
            bill.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class BillListView(generics.ListAPIView):
    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = Bill.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class BillDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Bill.objects.all()
    serializer_class = BillSaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# bill general items
# ----------------------------------------------------------------------------------------------------------

class GeneralView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = GeneralSerializer
        queryset = General.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = GeneralSerializer(data=request.data)
        if serializer.is_valid():
            general = General(
                bill=Bill.objects.get(id=request.data.get("bill_id")),
                item=request.data.get("item"),
                amount=request.data.get("amount"),
            )
            general.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class GeneralListView(generics.ListAPIView):
    serializer_class = GeneralSerializer

    def get_queryset(self):
        queryset = General.objects.all()
        bill = self.request.query_params.get('bill', None)
        if bill is not None:
            queryset = queryset.filter(bill=bill)
        return queryset

class GeneralDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = General.objects.all()
    serializer_class = GeneralSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# patient and admission select grid list
# --------------------------------------------------------------------------------------------------

class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class AdmissionListView(generics.ListAPIView):
    serializer_class = AdmissionSerializer

    def get_queryset(self):
        queryset = Admission.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset
