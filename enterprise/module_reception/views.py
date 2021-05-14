from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Visitor
from .serializers import VisitorSerializer


# Create your views here.

class VisitorView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        visitor = Visitor.objects.filter(account=account)
        serializer = VisitorSerializer(visitor, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class VisitorDetailView(APIView):
    def get(self, request, pk, format=None):
        visitor = Visitor.objects.get(pk=pk)
        serializer = VisitorSerializer(visitor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        visitor = Visitor.objects.get(pk=pk)
        serializer = VisitorSerializer(visitor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        visitor = Visitor.objects.get(pk=pk)
        visitor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
