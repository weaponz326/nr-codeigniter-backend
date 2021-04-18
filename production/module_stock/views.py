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
            item = StockItem(
                account=Profile.objects.get(id=request.data.get("production_id")),
                material_name=request.data.get("material_name"),
                location=request.data.get("location"),
                container=request.data.get("container"),
                bin_number=request.data.get("bin_number"),
                quantity=request.data.get("quantity"),
            )
            item.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class StockItemListView(generics.ListAPIView):
    serializer_class = StockItemSerializer

    def get_queryset(self):
        queryset = StockItem.objects.all()
        production = self.request.query_params.get('user', None)
        if production is not None:
            queryset = queryset.filter(account=production)
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
