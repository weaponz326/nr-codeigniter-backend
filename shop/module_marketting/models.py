from django.db import models

from accounts.models import Profile


# Create your models here.

class Campaign(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    campaign_code = models.CharField(max_length=20, blank=True)
    campaign_name = models.CharField(max_length=100, blank=True)
    campaign_type = models.CharField(max_length=50, blank=True)
    target_audience = models.TextField(blank=True)
    campaign_status = models.CharField(max_length=30, blank=True)
    supervisor = models.CharField(max_length=100, blank=True)
    goals = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)