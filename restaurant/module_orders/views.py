from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Order, OrderItem
from accounts.models import Profile
from module_menu.models import MenuItem
from .serializers import OrderSerializer, OrderItemSerializer, MenuItemSerializer


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
                restaurant=Profile.objects.get(id=request.data.get("restaurant_id")),
                order_code=request.data.get("order_code"),
                order_date=request.data.get("order_date"),
                customer_name=request.data.get("customer_name"),
                order_type=request.data.get("order_type"),
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
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(restaurant=restaurant)
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

# --------------------------------------------------------------------------------------------------
# order item

class OrderItemView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = OrderItemSerializer
        queryset = OrderItem.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            item = OrderItem(
                order=Order.objects.get(id=request.data.get("order_id")),
                menu_item=MenuItem.objects.get(id=request.data.get("menu_item_id")),
                item_code=request.data.get("order_code"),
                quantity=request.data.get("quantity"),
            )
            item.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class OrderItemListView(generics.ListAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        queryset = OrderItem.objects.all()
        order = self.request.query_params.get('order', None)
        if order is not None:
            queryset = queryset.filter(order=order)
        return queryset

class OrderItemDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# -------------------------------------------------------------------------------------------------

# get menu item list for dropdown select

class MenuItemListView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        restaurant = self.request.query_params.get('restaurant', None)
        if restaurant is not None:
            queryset = queryset.filter(restaurant=restaurant)
        return queryset
