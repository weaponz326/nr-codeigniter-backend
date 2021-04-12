from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Product
from accounts.models import Profile
from .serializers import ProductSerializer


# Create your views here.

class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ProductSerializer
        queryset = Product.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = Product(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                product_code=request.data.get("product_code"),
                product_name=request.data.get("product_name"),
                description=request.data.get("description"),
                location=request.data.get("location"),
                price=request.data.get("price"),
                stock=request.data.get("stock"),
            )
            product.save()
            latest_product = Product.objects.latest("id")

            return Response({
                'status': True,
                'product_id': latest_product.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class ProductDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
