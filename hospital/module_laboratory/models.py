from django.db import models

from accounts.models import Profile
from module_patients.models import Patient
from module_doctors.models import Doctor


# Create your models here.

class Laboratory(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    lab_code = models.CharField(max_length=50, blank=True)
    lab_date = models.DateField(null=True, blank=True)
    lab_type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)
