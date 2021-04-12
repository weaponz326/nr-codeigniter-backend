from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Sales
from accounts.models import Profile
from module_products.models import Product
from .serializers import SalesSerializer


# Create your views here.

class SalesView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = SalesSerializer
        queryset = Sales.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            sales = Sales(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                product=Profile.objects.get(id=request.data.get("product_id")),
                sales_code=request.data.get("sales_code"),
                sales_date=request.data.get("sales_date"),
                unit_price=request.data.get("unit_price"),
                quantity=request.data.get("quantity"),
            )
            sales.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class SalesListView(generics.ListAPIView):
    serializer_class = SalesSerializer

    def get_queryset(self):
        queryset = Sales.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class SalesDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
