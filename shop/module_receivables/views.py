from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Receivable
from accounts.models import Profile
from .serializers import ReceivableSerializer


# Create your views here.

class ReceivableView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ReceivableSerializer
        queryset = Receivable.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ReceivableSerializer(data=request.data)
        if serializer.is_valid():
            receivable = Receivable(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                receivable_code=request.data.get("receivable_code"),
                receivable_date=request.data.get("receivable_date"),
                due_date=request.data.get("due_date"),
                invoice_number=request.data.get("invoice_number"),
                customer_name=request.data.get("customer_name"),
                amount=request.data.get("amount"),
                date_received=request.data.get("date_received")
            )
            receivable.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ReceivableListView(generics.ListAPIView):
    serializer_class = ReceivableSerializer

    def get_queryset(self):
        queryset = Receivable.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class ReceivableDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Receivable.objects.all()
    serializer_class = ReceivableSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
