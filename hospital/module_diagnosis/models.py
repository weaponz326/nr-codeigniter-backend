from django.db import models

from accounts.models import Profile
from module_patients.models import Patient
from module_doctors.models import Doctor


# Create your models here.

class Diagnosis(models.Model):
    hospital = models.ForeignKey(Profile, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    diagnosis_code = models.CharField(max_length=50, blank=True)
    diagnosis_date = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=10, blank=True)
    temperature = models.CharField(max_length=10, blank=True)
    weight = models.CharField(max_length=10, blank=True)
    height = models.CharField(max_length=10, blank=True)
    blood_pressure = models.CharField(max_length=10, blank=True)
    pulse = models.CharField(max_length=10, blank=True)
    diagnosis_detail = models.TextField(blank=True)
    treatment = models.TextField(blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)

