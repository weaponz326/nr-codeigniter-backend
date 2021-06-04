from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Equipment
from accounts.models import Profile
from .serializers import EquipmentSerializer


# Create your views here.

class EquipmentView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        equipment = Equipment.objects.filter(account=account)
        serializer = EquipmentSerializer(equipment, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class EquipmentDetailView(APIView):
    def get(self, request, pk, format=None):
        equipment = Equipment.objects.get(pk=pk)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        equipment = Equipment.objects.get(pk=pk)
        serializer = EquipmentSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        equipment = Equipment.objects.get(pk=pk)
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
