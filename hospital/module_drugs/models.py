from django.db import models

from accounts.models import Profile


# Create your models here.

class Drug(models.Model):
    hospital = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ndc_number = models.CharField(max_length=50, blank=True)
    drug_name = models.CharField(max_length=100, blank=True)
    generic_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    manufacturer = models.CharField(max_length=100, blank=True)
    unit_dose = models.CharField(max_length=100, blank=True)
    drug_type = models.CharField(max_length=100, blank=True)
    unit_price = models.CharField(max_length=20, blank=True)
    batch_number = models.CharField(max_length=50, blank=True)
    purchased_date = models.DateField(null=True, blank=True)
    initial_quantity = models.CharField(max_length=20, blank=True)
    dispensed_quantity = models.CharField(max_length=20, blank=True)
    remaining_quantity = models.CharField(max_length=20, blank=True)
    manufacturing_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    storage_location = models.CharField(max_length=100, blank=True)
    storage_bin = models.CharField(max_length=50, blank=True)
    refill_ordered = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)
