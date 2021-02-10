# a bill is either order, sitting or delivery 
# this is selected accorrding to bill type
# only one of the sources get inserted in db according to selected type

from django.db import models

from accounts.models import Profile
from module_orders.models import Order
from module_sittings.models import Sitting
from module_deliveries.models import Delivery


# Create your models here.

class Bill(models.Model):
    restaurant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    sitting = models.ForeignKey(Sitting, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, null=True, blank=True)
    bill_code = models.CharField(max_length=50, blank=True)
    bill_date = models.DateField(null=True, blank=True)
    bill_type = models.CharField(max_length=50, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)
