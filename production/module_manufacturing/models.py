from django.db import models

from accounts.models import Profile
from module_products.models import Product


# Create your models here.

class Manufacturing(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    manufacturing_code = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    quantity = models.CharField(max_length=20, blank=True)
    manufacturing_status = models.CharField(max_length=30, blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)