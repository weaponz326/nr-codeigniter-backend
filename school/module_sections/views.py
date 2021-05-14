from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Section
from .serializers import SectionSerializer, SectionListSerializer


# Create your views here.

class SectionView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        section = Section.objects.filter(account=account)
        serializer = SectionListSerializer(section, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SectionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class SectionDetailView(APIView):
    def get(self, request, pk, format=None):
        section = Section.objects.get(pk=pk)
        serializer = SectionListSerializer(section)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        section = Section.objects.get(pk=pk)
        serializer = SectionSerializer(section, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        section = Section.objects.get(pk=pk)
        section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
