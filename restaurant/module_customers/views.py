from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Customer
from accounts.models import Profile
from .serializers import CustomerSerializer, CustomerListSerializer


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
                account=Profile.objects.get(id=request.data.get("restaurant_id")),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                sex=request.data.get("sex"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
                state=request.data.get("state"),
                city=request.data.get("city"),
                post_code=request.data.get("post_code"),
                customer_code=request.data.get("customer_code"),
                religion=request.data.get("religion"),
                allergies=request.data.get("allergies"),
                preferences=request.data.get("preferences"),
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
    serializer_class = CustomerListSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
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
