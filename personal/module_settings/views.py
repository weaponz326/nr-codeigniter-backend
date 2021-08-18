from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import ExtendedProfile
from .serializers import ExtendedProfileSerializer

# Create your views here.


class ExtendedProfileView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        extended_profile = ExtendedProfile.objects.filter(user=user)
        serializer = ExtendedProfileSerializer(extended_profile, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExtendedProfileSerializer(data=request.data)
        if serializer.is_valid():
            id=request.data.get("id")
            serializer.id=id
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ExtendedProfileDetailView(APIView):
    def get(self, request, pk, format=None):
        extended_profile = ExtendedProfile.objects.get(pk=pk)
        serializer = ExtendedProfileSerializer(extended_profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        extended_profile = ExtendedProfile.objects.get(pk=pk)
        serializer = ExtendedProfileSerializer(extended_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        extended_profile = ExtendedProfile.objects.get(pk=pk)
        extended_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
