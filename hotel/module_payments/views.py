from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Payment
from accounts.models import Profile
from .serializers import PaymentSerializer


# Create your views here.

class PaymentView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = PaymentSerializer
        queryset = Payment.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment = Payment(
                account=Profile.objects.get(id=request.data.get("hotel_id")),
                bill=Profile.objects.get(id=request.data.get("bill")),
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
            return Response({ 'status': False, 'errors': serializer.errors })

class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        hotel = self.request.query_params.get('user', None)
        if hotel is not None:
            queryset = queryset.filter(account=hotel)
        return queryset

class PaymentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
