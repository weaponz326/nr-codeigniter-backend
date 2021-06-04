from django.db import models

from accounts.models import Profile
from module_products.models import Product

# Create your models here.

class Order(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    order_code = models.CharField(max_length=20, blank=True)
    order_date = models.DateField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    quantity = models.CharField(max_length=30, blank=True)
    order_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)