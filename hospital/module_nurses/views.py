from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Nurse
from .serializers import NurseSerializer, NurseListSerializer


# Create your views here.

class NurseView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        nurse = Nurse.objects.filter(account=account)
        serializer = NurseListSerializer(nurse, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class NurseDetailView(APIView):
    def get(self, request, pk, format=None):
        nurse = Nurse.objects.get(pk=pk)
        serializer = NurseSerializer(nurse)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        nurse = Nurse.objects.get(pk=pk)
        serializer = NurseSerializer(nurse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        nurse = Nurse.objects.get(pk=pk)
        nurse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
