from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Folder, File
from accounts.models import Profile
from .serializers import FolderSerializer, FileSerializer


# Create your views here.

# folders

class FolderView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        folder = Folder.objects.filter(account=account)
        serializer = FolderSerializer(folder, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class FolderDetailView(APIView):
    def get(self, request, pk, format=None):
        folder = Folder.objects.get(pk=pk)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        folder = Folder.objects.get(pk=pk)
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        folder = Folder.objects.get(pk=pk)
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------------------
# files

class FileView(APIView):
    def get(self, request, format=None):
        folder = self.request.query_params.get('folder', None)
        file = File.objects.filter(folder=folder)
        serializer = FileSerializer(file, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class FileDetailView(APIView):
    def get(self, request, pk, format=None):
        file = File.objects.get(pk=pk)
        serializer = FileSerializer(file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        file = File.objects.get(pk=pk)
        serializer = FileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        file = File.objects.get(pk=pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
