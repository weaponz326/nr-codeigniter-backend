from django.db import models

from accounts.models import Profile
from module_prescriptions.models import Prescription
from module_drugs.models import Drug


# Create your models here.

class Dispensary(models.Model):
    hospital = models.ForeignKey(Profile, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True, blank=True)
    dispense_code = models.CharField(max_length=50, blank=True)
    dispense_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Detail(models.Model):
    dispensary = models.ForeignKey(Dispensary, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
