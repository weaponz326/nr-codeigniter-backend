from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Delivery
from accounts.models import Profile
from module_orders.models import Order
from .serializers import DeliverySerializer, OrderSerializer, DeliverySaveSerializer


# Create your views here.

class DeliveryView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = DeliverySerializer
        queryset = Delivery.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = DeliverySaveSerializer(data=request.data)
        if serializer.is_valid():
            delivery = Delivery(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                order=Patient.objects.get(id=request.data.get("order_id")),
                delivery_code=request.data.get("delivery_code"),
                delivery_date=request.data.get("delivery_date"),
                delivery_status=request.data.get("delivery_status")
            )
            delivery.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class DeliveryListView(generics.ListAPIView):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        queryset = Delivery.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
        return queryset

class DeliveryDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Delivery.objects.all()
    serializer_class = DeliverySaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# order select grid list
class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
        return queryset
