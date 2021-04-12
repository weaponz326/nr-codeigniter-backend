from django.contrib import admin

from .models import Campaign


# Register your models here.

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'campaign_code', 'campaign_name', 'campaign_status', 'start_date')

admin.site.register(Campaign, CampaignAdmin)
