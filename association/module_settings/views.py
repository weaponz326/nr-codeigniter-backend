from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import ExtendedProfile
from accounts.models import Profile
from .serializers import ProfileSerializer, ExtendedProfileSerializer


# Create your views here.

# retrieve and update basic profile

# profile
class ProfileDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

# retrieve extended profile 
class ExtendedProfileDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView):

    queryset = ExtendedProfile.objects.all()
    serializer_class = ExtendedProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# update profile
class ProfileView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# create or update extended profile
# update happens according to either location, or contact profile

class LocationExtendedView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ExtendedProfileSerializer(data=request.data)
        if serializer.is_valid():
            location_details = ExtendedProfile(
                profile=Profile.objects.get(id=request.data.get("profile")),
                country=request.data.get("country"),
                state=request.data.get("state"),
                city=request.data.get("city"),
            )
            location_details.id = request.data.get("profile")
            location_details.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False })

class ContactExtendedView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ContactProfileSerializer(data=request.data)
        if serializer.is_valid():
            contact_details = ExtendedProfile(
                profile=Profile.objects.get(id=request.data.get("profile")),
                phone1=request.data.get("phone1"),
                phone2=request.data.get("phone2"),
                email=request.data.get("email"),
                address=request.data.get("address"),
            )
            contact_details.id = request.data.get("profile")
            contact_details.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False })
