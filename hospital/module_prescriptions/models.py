from django.db import models

from accounts.models import Profile
from module_patients.models import Patient
from module_doctors.models import Doctor


# Create your models here.

class Prescription(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    prescription_code = models.CharField(max_length=50, blank=True)
    prescription_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class PrescriptionDetail(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine = models.TextField(blank=True)
    dosage = models.TextField(blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
