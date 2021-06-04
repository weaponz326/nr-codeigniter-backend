from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Manufacturing
from accounts.models import Profile
from .serializers import ManufacturingSerializer


# Create your views here.

class ManufacturingView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        manufacturing = Manufacturing.objects.filter(account=account)
        serializer = ManufacturingSerializer(manufacturing, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ManufacturingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ManufacturingDetailView(APIView):
    def get(self, request, pk, format=None):
        manufacturing = Manufacturing.objects.get(pk=pk)
        serializer = ManufacturingSerializer(manufacturing)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        manufacturing = Manufacturing.objects.get(pk=pk)
        serializer = ManufacturingSerializer(manufacturing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        manufacturing = Manufacturing.objects.get(pk=pk)
        manufacturing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
