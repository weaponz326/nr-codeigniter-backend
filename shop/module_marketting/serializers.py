from rest_framework import serializers

from .models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id', 
            'campaign_code', 
            'campaign_name', 
            'campaign_type', 
            'target_audience', 
            'campaign_status', 
            'supervisor', 
            'goals',
            'start_date',
            'end_date',
        ]
