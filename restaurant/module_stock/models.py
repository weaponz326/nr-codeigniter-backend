from django.db import models

from accounts.models import Profile


# Create your models here.

class StockItem(models.Model):
    restaurant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=20, blank=True)
    item_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=50, blank=True)
    item_type = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField(blank=True)
    refill_ordered = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.id)
