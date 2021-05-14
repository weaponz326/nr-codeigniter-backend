from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Parent, ParentWard
from .serializers import ParentSerializer, ParentListSerializer, ParentWardSerializer, ParentWardListSerializer


# Create your views here.

class ParentView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        parent = Parent.objects.filter(account=account)
        serializer = ParentListSerializer(parent, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ParentDetailView(APIView):
    def get(self, request, pk, format=None):
        parent = Parent.objects.get(pk=pk)
        serializer = ParentSerializer(parent)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        parent = Parent.objects.get(pk=pk)
        serializer = ParentSerializer(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        parent = Parent.objects.get(pk=pk)
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# parent wards
# -----------------------------------------------------------------------------------------------------------

class ParentWardView(APIView):
    def get(self, request, format=None):
        parent = self.request.query_params.get('parent', None)
        ward = ParentWard.objects.filter(parent=parent)
        serializer = ParentWardListSerializer(ward, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ParentWardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ParentWardDetailView(APIView):
    def get(self, request, pk, format=None):
        ward = ParentWard.objects.get(pk=pk)
        serializer = ParentWardListSerializer(ward)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ward = ParentWard.objects.get(pk=pk)
        serializer = ParentWardSerializer(ward, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        ward = ParentWard.objects.get(pk=pk)
        ward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
