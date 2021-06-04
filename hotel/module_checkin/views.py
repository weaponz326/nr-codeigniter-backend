from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Checkin
from accounts.models import Profile
from .serializers import CheckinSerializer


# Create your views here.

class CheckinView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        checkin = Checkin.objects.filter(account=account)
        serializer = CheckinSerializer(checkin, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CheckinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class CheckinDetailView(APIView):
    def get(self, request, pk, format=None):
        checkin = Checkin.objects.get(pk=pk)
        serializer = CheckinSerializer(checkin)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        checkin = Checkin.objects.get(pk=pk)
        serializer = CheckinSerializer(checkin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        checkin = Checkin.objects.get(pk=pk)
        checkin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
