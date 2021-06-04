from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Asset
from .serializers import AssetSerializer


# Create your views here.

class AssetView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        asset = Asset.objects.filter(account=account)
        serializer = AssetSerializer(asset, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AssetDetailView(APIView):
    def get(self, request, pk, format=None):
        asset = Asset.objects.get(pk=pk)
        serializer = AssetSerializer(asset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        asset = Asset.objects.get(pk=pk)
        serializer = AssetSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        asset = Asset.objects.get(pk=pk)
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
