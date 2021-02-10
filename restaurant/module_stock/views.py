from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import StockItem
from accounts.models import Profile
from .serializers import StockItemSerializer


# Create your views here.

class StockItemView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = StockItemSerializer
        queryset = StockItem.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = StockItemSerializer(data=request.data)
        if serializer.is_valid():
            menu = StockItem(
                restaurant=Profile.objects.get(id=request.data.get("restaurant_id")),
                item_code=request.data.get("item_code"),
                item_name=request.data.get("item_name"),
                category=request.data.get("category"),
                item_type=request.data.get("item_type"),
                quantity=request.data.get("quantity"),
                refill_ordered=request.data.get("refill_ordered"),
            )
            menu.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class StockItemListView(generics.ListAPIView):
    serializer_class = StockItemSerializer

    def get_queryset(self):
        queryset = StockItem.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(restaurant=restaurant)
        return queryset

class StockItemDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
