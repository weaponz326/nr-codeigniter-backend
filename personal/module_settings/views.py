from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import AdditionalProfile, LocationDetails, Contact
from users.models import Profile
from .serializers import ProfileUserSerializer, UserSerializer, ProfileSerializer, AdditionalProfileSerializer, LocationDetailsSerializer, ContactSerializer

# Create your views here.

# retrieve basic profile
class ProfileUserView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUserSerializer

# retrieve additional profile and contact details with pk

class AdditionalProfileDetailView(generics.RetrieveAPIView):
    queryset = AdditionalProfile.objects.all()
    serializer_class = AdditionalProfileSerializer

class LocationDetailsDetailView(generics.RetrieveAPIView):
    queryset = LocationDetails.objects.all()
    serializer_class = LocationDetailsSerializer

# update user and profile
# both apis are called at the same time to prevent updating nested serializer

class UserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# create or update additional porfile and contact details

class AdditionalProfileView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = AdditionalProfileSerializer(data=request.data)
        if serializer.is_valid():
            additional_profile = AdditionalProfile(
                user=User.objects.get(id=request.data.get("user")),
                date_of_birth=request.data.get("date_of_birth"),
                gender=request.data.get("gender"),
            )
            additional_profile.id = request.data.get("user")
            additional_profile.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False })

class LocationDetailsView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = LocationDetailsSerializer(data=request.data)
        if serializer.is_valid():
            contact_details = LocationDetails(
                user=User.objects.get(id=request.data.get("user")),
                country=request.data.get("country"),
                state=request.data.get("state"),
                city=request.data.get("city"),
            )
            contact_details.id = request.data.get("user")
            contact_details.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False })
