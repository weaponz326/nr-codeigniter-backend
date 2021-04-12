from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Supplier
from accounts.models import Profile
from .serializers import SupplierSerializer


# Create your views here.

class SupplierView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = SupplierSerializer
        queryset = Supplier.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            supplier = Supplier(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                supplier_code=request.data.get("supplier_code"),
                supplier_name=request.data.get("supplier_name"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
            )
            supplier.save()
            latest_supplier = Supplier.objects.latest("id")

            return Response({
                'status': True,
                'supplier_id': latest_supplier.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class SupplierListView(generics.ListAPIView):
    serializer_class = SupplierSerializer

    def get_queryset(self):
        queryset = Supplier.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class SupplierDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
