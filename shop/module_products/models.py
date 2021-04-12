from django.db import models

from accounts.models import Profile


# Create your models here.

class Product(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=20, blank=True)
    product_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=15, blank=True)
    stock = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)