from django.db import models

from accounts.models import Profile


# Create your models here.

class Purchasing(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    purchasing_code = models.CharField(max_length=20, blank=True)
    purchasing_date = models.DateField(null=True, blank=True)
    supplier_name = models.CharField(max_length=100, blank=True)
    supplier_contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)

class PurchasingItem(models.Model):
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, blank=True)
    quantity = models.CharField(max_length=20, blank=True)
    total_price = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)