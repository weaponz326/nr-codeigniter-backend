from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Payment
from accounts.models import Profile
from module_patients.models import Patient
from module_admissions.models import Admission
from module_bills.models import Bill
from .serializers import (
    PaymentSerializer, 
    PaymentSaveSerializer, 
    PatientSerializer, 
    AdmissionSerializer,
    BillSerializer
)


# Create your views here.

# create a new payment for the first time
class NewPaymentView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PaymentSaveSerializer(data=request.data)
        if serializer.is_valid():
            payment = Payment(
                hospital=Profile.objects.get(id=request.data.get("hospital_id")),
                patient=Patient.objects.get(id=request.data.get("patient_id")),
                admission=Admission.objects.get(id=request.data.get("admission_id")),
                bill=Bill.objects.get(id=request.data.get("bill_id")),
                payment_code=request.data.get("payment_code"),
                payment_date=request.data.get("payment_date"),
                amount_paid=request.data.get("amount_paid"),
                balance=request.data.get("balance"),
            )
            payment.save()
            latest_payment = Payment.objects.latest("id")

            return Response({
                'status': True,
                'payment_id': latest_payment.id
            })
        else:
            return Response({ 'status': False })

class PaymentView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = PaymentSerializer
        queryset = Payment.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = PaymentSaveSerializer(data=request.data)
        if serializer.is_valid():
            payment = Payment(
                hospital=Profile.objects.get(id=request.data.get("hospital_id")),
                patient=Patient.objects.get(id=request.data.get("patient_id")),
                admission=Admission.objects.get(id=request.data.get("admission_id")),
                bill=Bill.objects.get(id=request.data.get("bill_id")),
                payment_code=request.data.get("payment_code"),
                payment_date=request.data.get("payment_date"),
                amount_paid=request.data.get("amount_paid"),
                balance=request.data.get("balance"),
            )
            payment.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class PaymentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# patient,  admission and bill select grid list
# --------------------------------------------------------------------------------------------------

class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class AdmissionListView(generics.ListAPIView):
    serializer_class = AdmissionSerializer

    def get_queryset(self):
        queryset = Admission.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class BillListView(generics.ListAPIView):
    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = Bill.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset
