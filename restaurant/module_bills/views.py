from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Bill
from accounts.models import Profile
from module_orders.models import Order
from module_sittings.models import Sitting
from module_deliveries.models import Delivery
from .serializers import (
    BillSerializer, 
    BillSaveSerializer, 
    OrderSerializer,
    SittingSerializer,
    DeliverySerializer
)


# Create your views here.

# create a new bill for the first time
class NewBillView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BillSaveSerializer(data=request.data)
        if serializer.is_valid():
            bill = Bill(
                account=Profile.objects.get(id=request.data.get("restaurant_id")),
                order=Order.objects.get(id=request.data.get("order_id")),
                sitting=Sitting.objects.get(id=request.data.get("sitting_id")),
                delivery=Delivery.objects.get(id=request.data.get("delivery_id")),
                bill_code=request.data.get("bill_code"),
                bill_date=request.data.get("bill_date"),
                bill_type=request.data.get("bill_type"),
                customer_name=request.data.get("customer_name"),
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
                account=Profile.objects.get(id=request.data.get("restaurant_id")),
                order=Order.objects.get(id=request.data.get("order_id")),
                sitting=Sitting.objects.get(id=request.data.get("sitting_id")),
                delivery=Delivery.objects.get(id=request.data.get("delivery_id")),
                bill_code=request.data.get("bill_code"),
                bill_date=request.data.get("bill_date"),
                bill_type=request.data.get("bill_type"),
                customer_name=request.data.get("customer_name"),
            )
            bill.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class BillListView(generics.ListAPIView):
    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = Bill.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
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

# order, sitting, delivery select grid list
# --------------------------------------------------------------------------------------------------

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
        return queryset

class SittingListView(generics.ListAPIView):
    serializer_class = SittingSerializer

    def get_queryset(self):
        queryset = Sitting.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
        return queryset

class DeliveryListView(generics.ListAPIView):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        queryset = Delivery.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
        return queryset

