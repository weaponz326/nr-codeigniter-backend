from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Campaign
from accounts.models import Profile
from .serializers import CampaignSerializer


# Create your views here.

class CampaignView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CampaignSerializer
        queryset = Campaign.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            campaign = Campaign(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                campaign_code=request.data.get("campaign_code"),
                campaign_name=request.data.get("campaign_name"),
                campaign_type=request.data.get("campaign_type"),
                target_audience=request.data.get("target_audience"),
                campaign_status=request.data.get("campaign_status"),
                supervisor=request.data.get("supervisor"),
                goals=request.data.get("goals"),
                start_date=request.data.get("start_date"),
                end_date=request.data.get("end_date"),
            )
            campaign.save()
            latest_campaign = Campaign.objects.latest("id")

            return Response({
                'status': True,
                'campaign_id': latest_campaign.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class CampaignListView(generics.ListAPIView):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        queryset = Campaign.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class CampaignDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
