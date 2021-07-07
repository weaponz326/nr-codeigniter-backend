from django.db import models

from accounts.models import Profile
from module_menu.models import MenuItem


# Create your models here.

class Order(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_code = models.CharField(max_length=50, blank=True)
    order_date = models.DateField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    order_type = models.CharField(max_length=50, blank=True)
    order_status = models.CharField(max_length=50, blank=True)
    order_total = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
