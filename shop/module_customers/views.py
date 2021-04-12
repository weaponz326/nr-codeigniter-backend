from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Customer
from accounts.models import Profile
from .serializers import CustomerSerializer


# Create your views here.

class CustomerView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CustomerSerializer
        queryset = Customer.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = Customer(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                customer_code=request.data.get("customer_code"),
                customer_name=request.data.get("customer_name"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
            )
            customer.save()
            latest_customer = Customer.objects.latest("id")

            return Response({
                'status': True,
                'customer_id': latest_customer.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class CustomerListView(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class CustomerDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
