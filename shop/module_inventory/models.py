from django.db import models

from accounts.models import Profile
from module_products.models import Product

# Create your models here.

class InventoryItem(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    container = models.CharField(max_length=50, blank=True)
    bin_number = models.CharField(max_length=50, blank=True)
    quantity = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return str(self.id)