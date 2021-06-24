from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Guest
from .serializers import GuestSerializer, GuestListSerializer


# Create your views here.

class GuestView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        guest = Guest.objects.filter(account=account)
        serializer = GuestListSerializer(guest, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class GuestDetailView(APIView):
    def get(self, request, pk, format=None):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        guest = Guest.objects.get(pk=pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
