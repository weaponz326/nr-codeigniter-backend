from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Invoice, InvoiceItem
from accounts.models import Profile
from .serializers import InvoiceSerializer


# Create your views here.

class InvoiceView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = InvoiceSerializer
        queryset = Invoice.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            invoice = Invoice(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                invoice_number=request.data.get("invoice_number"),
                invoice_date=request.data.get("invoice_date"),
                customer_name=request.data.get("customer_name"),
                customer_contact=request.data.get("customer_contact"),
                due_date=request.data.get("due_date"),
            )
            invoice.save()
            latest_invoice = Invoice.objects.latest("id")

            return Response({
                'status': True,
                'invoice_id': latest_invoice.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class InvoiceListView(generics.ListAPIView):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class InvoiceDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
