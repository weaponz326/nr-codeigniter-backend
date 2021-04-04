from django.db import models

from accounts.models import Profile


# Create your models here.

class Procurement(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_code = models.CharField(max_length=20, blank=True)
    order_date = models.DateField(null=True, blank=True)
    order_type = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    project = models.CharField(max_length=100, blank=True)
    recepient = models.CharField(max_length=100, blank=True)
    vendor = models.CharField(max_length=100, blank=True)
    vendor_phone = models.CharField(max_length=20, blank=True)
    vendor_email = models.CharField(max_length=100, blank=True)
    vendor_address = models.TextField(blank=True)
    order_status = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)
