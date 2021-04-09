from django.db import models

from accounts.models import Profile


# Create your models here.

class Service(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service_code = models.CharField(max_length=20, blank=True)
    service_type = models.CharField(max_length=100, blank=True)
    service_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    item_date = models.DateField(null=True, blank=True)
    item_description = models.TextField(blank=True)
    amount = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)
