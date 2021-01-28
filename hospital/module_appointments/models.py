from django.db import models

from accounts.models import Profile
from module_patients.models import Patient
from module_doctors.models import Doctor


# Create your models here.

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'), 
        ('Ongoing', 'Ongoing'),
        ('Finished', 'Finished'),
        ('Cancelled', 'Cancelled'),
    ]

    hospital = models.ForeignKey(Profile, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    consultant = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    appointment_code = models.CharField(max_length=50, blank=True)
    appointment_date = models.DateField(null=True, blank=True)
    appointment_for = models.CharField(max_length=100, blank=True)
    remarks = models.TextField(max_length=100, blank=True)
    appointment_status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True)

    def __str__(self):
        return str(self.id)