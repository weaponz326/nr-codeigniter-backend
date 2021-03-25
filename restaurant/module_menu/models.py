from django.db import models

from accounts.models import Profile


# Create your models here.

class MenuItem(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=20, blank=True)
    item_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
