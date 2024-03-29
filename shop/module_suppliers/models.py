from django.db import models

from accounts.models import Profile
from module_products.models import Product


# Create your models here.

class Supplier(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    supplier_code = models.CharField(max_length=20, blank=True)
    supplier_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)

class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)        