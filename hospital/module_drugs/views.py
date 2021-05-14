from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Drug
from .serializers import DrugSerializer


# Create your views here.

class DrugView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        drug = Drug.objects.filter(account=account)
        serializer = DrugSerializer(drug, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DrugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DrugDetailView(APIView):
    def get(self, request, pk, format=None):
        drug = Drug.objects.get(pk=pk)
        serializer = DrugSerializer(drug)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        drug = Drug.objects.get(pk=pk)
        serializer = DrugSerializer(drug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        drug = Drug.objects.get(pk=pk)
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
