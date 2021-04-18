from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Order
from accounts.models import Profile
from module_products.models import Product
from .serializers import OrderSerializer


# Create your views here.

class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = OrderSerializer
        queryset = Order.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = Order(
                account=Profile.objects.get(id=request.data.get("production_id")),
                product=Profile.objects.get(id=request.data.get("product_id")),
                order_code=request.data.get("order_code"),
                order_date=request.data.get("order_date"),
                customer_name=request.data.get("customer_name"),
                quantity=request.data.get("quantity"),
                order_status=request.data.get("order_status"),
            )
            order.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        production = self.request.query_params.get('user', None)
        if production is not None:
            queryset = queryset.filter(account=production)
        return queryset

class OrderDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
