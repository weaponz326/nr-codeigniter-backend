from django.db import models

from accounts.models import Profile
from module_orders.models import Order


# Create your models here.

class Payment(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_code = models.CharField(max_length=20, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    payment = models.CharField(max_length=20, blank=True)
    

    def __str__(self):
        return str(self.id)