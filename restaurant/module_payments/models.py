from django.db import models

from accounts.models import Profile
from module_bills.models import Bill


# Create your models here.

class Payment(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True, blank=True)
    payment_code = models.CharField(max_length=50, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    balance = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)
