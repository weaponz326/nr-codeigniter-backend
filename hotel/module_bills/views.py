from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Bill
from accounts.models import Profile
from module_guests.models import Guest
from .serializers import BillSerializer


# Create your views here.

class BillView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = BillSerializer
        queryset = Bill.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            bill = Bill(
                account=Profile.objects.get(id=request.data.get("hotel_id")),
                guest=Guests.objects.get(id=request.data.get("guest")),
                bill_code=request.data.get("bill_code"),
                bill_date=request.data.get("bill_date"),
            )
            bill.save()
            latest_bill = Bill.objects.latest("id")

            return Response({
                'status': True,
                'bill_id': latest_bill.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class BillListView(generics.ListAPIView):
    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = Bill.objects.all()
        hotel = self.request.query_params.get('user', None)
        if hotel is not None:
            queryset = queryset.filter(account=hotel)
        return queryset

class BillDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
