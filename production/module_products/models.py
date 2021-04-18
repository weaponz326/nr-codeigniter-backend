from django.db import models

from accounts.models import Profile


# Create your models here.

class Product(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=20, blank=True)
    product_name = models.CharField(max_length=100, blank=True)
    product_type = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=100, blank=True)
    model_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)