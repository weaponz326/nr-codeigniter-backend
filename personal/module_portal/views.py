from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters

# from .models import 
from .serializers import ProfileSerializer


# Create your views here.

class SearchListView(generics.ListCreateAPIView):
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter, )
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    
    
    
    # serializer_class = TaskSerializer

    # def get_queryset(self):
    #     queryset = User.objects.all()
    #     user = self.request.query_params.get('user', None)
    #     if user is not None:
    #         queryset = queryset.filter(user=user)
    #     return queryset