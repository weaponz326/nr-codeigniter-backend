from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import SettingsProfileSerializer
from users.serializers import ProfileSerializer


# Create your views here.

# List settings all profiles or create new profile
class SettingsProfileView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = SettingsProfileSerializer
        queryset = Profile.objects.all()
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SettingsProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializers.errors)

# retrive, update and delete a single settings profile
class SettingsProfileDetailView(APIView):
    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = SettingsProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = SettingsProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializers.errors)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status)

# retrive, update and delete a single users profile
class ProfileDetailView(APIView):
    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializers.errors)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status)
