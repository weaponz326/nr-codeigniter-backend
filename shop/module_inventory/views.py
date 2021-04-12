from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import InventoryItem
from accounts.models import Profile
from module_products.models import Product
from .serializers import InventoryItemSerializer


# Create your views here.

class InventoryItemView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = InventoryItemSerializer
        queryset = InventoryItem.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            item = InventoryItem(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                product=Profile.objects.get(id=request.data.get("product_id")),
                location=request.data.get("location"),
                container=request.data.get("container"),
                bin_number=request.data.get("bin_number"),
                quantity=request.data.get("quantity"),
            )
            item.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class InventoryItemListView(generics.ListAPIView):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        queryset = InventoryItem.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class InventoryItemDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
