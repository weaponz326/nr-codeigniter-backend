from django.db import models

from accounts.models import Profile
from module_products.models import Product

# Create your models here.

class Sales(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales_code = models.CharField(max_length=20, blank=True)
    sales_date = models.DateTimeField(null=True, blank=True)
    unit_price = models.CharField(max_length=20, blank=True)
    quantity = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return str(self.id)