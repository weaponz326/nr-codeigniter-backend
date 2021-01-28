from django.db import models

from accounts.models import Profile
from module_patients.models import Patient


# Create your models here.

class Admission(models.Model):
    hospital = models.ForeignKey(Profile, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    admission_code = models.CharField(max_length=50, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    discharge_date = models.DateField(null=True, blank=True)
    admission_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)
