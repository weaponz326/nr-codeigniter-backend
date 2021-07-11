from django.db import models

from accounts.models import Profile
from module_bills.models import Bill

# Create your models here.

class Payment(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, null=True, on_delete=models.CASCADE)
    payment_code = models.CharField(max_length=20, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    payment = models.CharField(max_length=20, blank=True)
    balance = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)
