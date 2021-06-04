from django.db import models

from accounts.models import Profile
from module_products.models import Product

# Create your models here.

class Invoice(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=20, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    customer_contact = models.CharField(max_length=20, blank=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20, blank=True)
    total_price = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)