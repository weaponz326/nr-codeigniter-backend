from django.db import models

from accounts.models import Profile
from module_products.models import Product

# Create your models here.

class Order(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_code = models.CharField(max_length=20, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    order_status = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20, blank=True)
    total_price = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)