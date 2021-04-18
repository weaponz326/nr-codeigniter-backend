from django.db import models

from accounts.models import Profile


# Create your models here.

class Equipment(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    equipment_code = models.CharField(max_length=20, blank=True)
    equipment_name = models.CharField(max_length=100, blank=True)
    equipment_type = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    serial_number = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    condition = models.CharField(max_length=50, blank=True)
    equipment_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)