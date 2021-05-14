from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Laboratory, Attachment
from .serializers import LaboratorySerializer, LaboratoryListSerializer


# Create your views here.

class LaboratoryView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        laboratory = Laboratory.objects.filter(account=account)
        serializer = LaboratoryListSerializer(laboratory, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LaboratorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class LaboratoryDetailView(APIView):
    def get(self, request, pk, format=None):
        laboratory = Laboratory.objects.get(pk=pk)
        serializer = LaboratoryListSerializer(laboratory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        laboratory = Laboratory.objects.get(pk=pk)
        serializer = LaboratorySerializer(laboratory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        laboratory = Laboratory.objects.get(pk=pk)
        laboratory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------------
# files

class AttachmentView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        attachment = Attachment.objects.filter(account=account)
        serializer = AttachmentListSerializer(attachment, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AttachmentDetailView(APIView):
    def get(self, request, pk, format=None):
        attachment = Attachment.objects.get(pk=pk)
        serializer = AttachmentListSerializer(attachment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        attachment = Attachment.objects.get(pk=pk)
        serializer = AttachmentSerializer(attachment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        attachment = Attachment.objects.get(pk=pk)
        attachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
