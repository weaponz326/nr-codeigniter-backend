from django.db import models

from accounts.models import Profile
from module_suppliers.models import Supplier
from module_products.models import Product

# Create your models here.

class Purchasing(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE)
    purchasing_code = models.CharField(max_length=20, blank=True)
    purchasing_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class PurchasingItem(models.Model):
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)