from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Term
from .serializers import TermSerializer


# Create your views here.

class TermView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        term = Term.objects.filter(account=account)
        serializer = TermSerializer(term, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TermSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class TermDetailView(APIView):
    def get(self, request, pk, format=None):
        term = Term.objects.get(pk=pk)
        serializer = TermSerializer(term)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        term = Term.objects.get(pk=pk)
        serializer = TermSerializer(term, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        term = Term.objects.get(pk=pk)
        term.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
