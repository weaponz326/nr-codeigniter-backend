from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, status

from .models import Rink
from .serializers import RinkSerializer


# Create your views here.

class RinkView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        account = Rink.objects.filter(account=account)
        serializer = RinkSerializer(account, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RinkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class RinkDetailView(APIView):
    def get(self, request, pk, format=None):
        rink = Rink.objects.get(pk=pk)
        serializer = RinkSerializer(rink)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rink = Rink.objects.get(pk=pk)
        serializer = RinkSerializer(rink, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        rink = Rink.objects.get(pk=pk)
        rink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# list all rinks of a account
class RinkListView(generics.ListAPIView):
    serializer_class = RinkSerializer

    def get_queryset(self):
        queryset = Rink.objects.all()
        account = self.request.query_params.get('account', None)
        if account is not None:
            queryset = queryset.filter(sender__id=account) | queryset.filter(recipient__id=account)
        return queryset
