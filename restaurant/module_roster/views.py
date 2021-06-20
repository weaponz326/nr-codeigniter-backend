from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Roster
from .serializers import RosterSerializer


# Create your views here.

class RosterView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        drug = Roster.objects.filter(account=account)
        serializer = RosterSerializer(drug, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RosterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class RosterDetailView(APIView):
    def get(self, request, pk, format=None):
        drug = Roster.objects.get(pk=pk)
        serializer = RosterSerializer(drug)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        drug = Roster.objects.get(pk=pk)
        serializer = RosterSerializer(drug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        drug = Roster.objects.get(pk=pk)
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
