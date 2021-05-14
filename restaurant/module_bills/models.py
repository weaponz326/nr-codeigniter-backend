from django.db import models

from accounts.models import Profile
from module_orders.models import Order


# Create your models here.

class Bill(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    bill_code = models.CharField(max_length=50, blank=True)
    bill_date = models.DateField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)
