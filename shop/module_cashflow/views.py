from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Sheet
from .serializers import SheetSerializer


# Create your views here.

class SheetView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        sheet = Sheet.objects.filter(account=account)
        serializer = SheetSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class SheetDetailView(APIView):
    def get(self, request, pk, format=None):
        sheet = Sheet.objects.get(pk=pk)
        serializer = SheetSerializer(sheet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sheet = Sheet.objects.get(pk=pk)
        serializer = SheetSerializer(sheet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        sheet = Sheet.objects.get(pk=pk)
        sheet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
