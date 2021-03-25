from django.db import models

from accounts.models import Profile
from module_orders.models import Order


# Create your models here.

class Delivery(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    delivery_code = models.CharField(max_length=50, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    delivery_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)