from django.db import models

from accounts.models import Profile
from module_patients.models import Patient


# Create your models here.

class Ward(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ward_number = models.CharField(max_length=50, blank=True)
    ward_name = models.CharField(max_length=100, blank=True)
    ward_type = models.CharField(max_length=50, blank=True)
    location = models.TextField(blank=True)
    capacity = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.id)

class WardPatient(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed_number = models.CharField(max_length=20, blank=True)
    date_admitted = models.DateField(null=True, blank=True)
    date_discharged = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)
