from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import filters

from .models import Rink
from accounts.models import Profile
from module_staff.models import Staff
from module_customers.models import Customer
from module_menu.models import MenuItem
from .serializers import RinkSerializer, ProfileSerializer, RinkDetailSerializer
from module_staff.serializers import StaffSerializer
from module_customers.serializers import CustomerSerializer
from module_menu.serializers import MenuItemSerializer


# Create your views here.

class RinkView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = RinkSerializer
        queryset = Rink.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = RinkSerializer(data=request.data)
        if serializer.is_valid():
            rink = Rink(
                sender=Profile.objects.get(id=request.data.get("sender")),
                recipient=Profile.objects.get(id=request.data.get("recipient")),
                rink_type=request.data.get("rink_type"),
                rink_source=request.data.get("rink_source"),
                comment=request.data.get("comment")
            )
            rink.save()
            latest_rink = Rink.objects.latest("id")

            return Response({ 
                'status': True ,
                'rink_id': latest_rink.id
            })
        else:
            return Response({ 'status': False })

class SearchListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
class SearchDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# rink type sources

class StaffListView(generics.ListAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        queryset = Staff.objects.all()
        restaurant = self.request.query_params.get('restaurant', None)
        if restaurant is not None:
            queryset = queryset.filter(restaurant=restaurant)
        return queryset

class CustomerListView(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        restaurant = self.request.query_params.get('restaurant', None)
        if restaurant is not None:
            queryset = queryset.filter(restaurant=restaurant)
        return queryset

class MenuListView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        restaurant = self.request.query_params.get('restaurant', None)
        if restaurant is not None:
            queryset = queryset.filter(restaurant=restaurant)
        return queryset

# list all rinks of a user
class RinkListView(generics.ListAPIView):
    serializer_class = RinkDetailSerializer

    def get_queryset(self):
        queryset = Rink.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            # queryset = queryset.filter(recipient__id=user).filter(sender__id=user)
            queryset = queryset.filter(recipient__id=user)
        return queryset

# get a specific rink
class RinkDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Rink.objects.all()
    serializer_class = RinkDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# get single dource for rink details

class StaffDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class CustomerDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class MenuDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

