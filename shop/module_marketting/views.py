from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Campaign
from .serializers import CampaignSerializer


# Create your views here.

class CampaignView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        campaign = Campaign.objects.filter(account=account)
        serializer = CampaignSerializer(campaign, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class CampaignDetailView(APIView):
    def get(self, request, pk, format=None):
        campaign = Campaign.objects.get(pk=pk)
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        campaign = Campaign.objects.get(pk=pk)
        serializer = CampaignSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        campaign = Campaign.objects.get(pk=pk)
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
