from django.db import models

from accounts.models import Profile

# Create your models here.

class StockItem(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    container = models.CharField(max_length=50, blank=True)
    bin_number = models.CharField(max_length=50, blank=True)
    quantity = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return str(self.id)