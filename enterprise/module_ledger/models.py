from django.db import models
from accounts.models import Profile


# Create your models here.

class Ledger(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ledger_name = models.CharField(max_length=100, blank=True)
    ledger_code = models.CharField(max_length=20, blank=True)
    ledger_date = models.DateField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class LedgerItem(models.Model):
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    item_date = models.DateField(null=True, blank=True)
    reference_number = models.CharField(max_length=20, blank=True)
    description = models.TextField(null=True)
    credit = models.CharField(max_length=20, blank=True)
    debit = models.CharField(max_length=20, blank=True)
    balance = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)
