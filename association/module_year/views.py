from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Year
from .serializers import YearSerializer


# Create your views here.

class YearView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        year = Year.objects.filter(account=account)
        serializer = YearSerializer(year, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = YearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class YearDetailView(APIView):
    def get(self, request, pk, format=None):
        year = Year.objects.get(pk=pk)
        serializer = YearSerializer(year)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        year = Year.objects.get(pk=pk)
        serializer = YearSerializer(year, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        year = Year.objects.get(pk=pk)
        year.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

