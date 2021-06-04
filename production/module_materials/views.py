from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Material
from .serializers import MaterialSerializer


# Create your views here.

class MaterialView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        material = Material.objects.filter(account=account)
        serializer = MaterialSerializer(material, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class MaterialDetailView(APIView):
    def get(self, request, pk, format=None):
        material = Material.objects.get(pk=pk)
        serializer = MaterialSerializer(material)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        material = Material.objects.get(pk=pk)
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        material = Material.objects.get(pk=pk)
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
