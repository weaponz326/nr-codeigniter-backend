from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Payable
from accounts.models import Profile
from .serializers import PayableSerializer


# Create your views here.

class PayableView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = PayableSerializer
        queryset = Payable.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = PayableSerializer(data=request.data)
        if serializer.is_valid():
            payable = Payable(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                payable_code=request.data.get("payable_code"),
                payable_date=request.data.get("payable_date"),
                due_date=request.data.get("due_date"),
                invoice_number=request.data.get("invoice_number"),
                customer_name=request.data.get("customer_name"),
                amount=request.data.get("amount"),
                date_paid=request.data.get("date_paid")
            )
            payable.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class PayableListView(generics.ListAPIView):
    serializer_class = PayableSerializer

    def get_queryset(self):
        queryset = Payable.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class PayableDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Payable.objects.all()
    serializer_class = PayableSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
