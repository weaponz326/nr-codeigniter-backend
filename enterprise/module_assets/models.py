from django.db import models

from accounts.models import Profile


# Create your models here.

class Asset(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    asset_code = models.CharField(max_length=20, blank=True)
    asset_name = models.CharField(max_length=100, blank=True)
    asset_type = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    date_purchased = models.DateField(null=True, blank=True)
    purchased_value = models.CharField(max_length=20, blank=True)
    supplier = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    serial_number = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    condition = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.id)
