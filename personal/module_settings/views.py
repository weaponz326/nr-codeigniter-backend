from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import ExtendedProfile
from users.models import Profile
from .serializers import UserSerializer, ProfileSerializer, ExtendedProfileSerializer

# Create your views here.

# retrieve and update basic profile

# user
class UserDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

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


# update user and profile
# both apis are called at the same time to prevent updating nested serializer

class UserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# create or update extended profile
# update happens according to either additional, location, or contact profile

class AdditionalExtendedView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ExtendedProfileSerializer(data=request.data)
        if serializer.is_valid():
            additional_profile = ExtendedProfile(
                user=User.objects.get(id=request.data.get("user")),
                date_of_birth=request.data.get("date_of_birth"),
                gender=request.data.get("gender"),
            )
            additional_profile.id = request.data.get("user")
            additional_profile.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False })

class LocationExtendedView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ExtendedProfileSerializer(data=request.data)
        if serializer.is_valid():
            location_details = ExtendedProfile(
                user=User.objects.get(id=request.data.get("user")),
                country=request.data.get("country"),
                state=request.data.get("state"),
                city=request.data.get("city"),
            )
            location_details.id = request.data.get("user")
            location_details.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False })

class ContactExtendedView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ContactProfileSerializer(data=request.data)
        if serializer.is_valid():
            contact_details = ExtendedProfile(
                user=User.objects.get(id=request.data.get("user")),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
            )
            contact_details.id = request.data.get("user")
            contact_details.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False })
