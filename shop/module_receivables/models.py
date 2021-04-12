from django.db import models

from accounts.models import Profile


# Create your models here.

class Receivable(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receivable_code = models.CharField(max_length=20, blank=True)
    receivable_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    invoice_number = models.CharField(max_length=30, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    amount = models.CharField(max_length=15, blank=True)
    date_received = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id)