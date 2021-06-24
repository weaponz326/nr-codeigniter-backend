from django.db import models

from accounts.models import Profile
from module_patients.models import Patient
from module_admissions.models import Admission
from module_appointments.models import Appointment
from module_laboratory.models import Laboratory
from module_dispensary.models import Dispensary
from module_wards.models import Ward


# Create your models here.

class Bill(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE, null=True, blank=True)
    bill_code = models.CharField(max_length=50, blank=True)
    bill_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)

class General(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)

class AppointmentCharge(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)

class LaboratoryCharge(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    lab = models.ForeignKey(Laboratory, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)

class DispensaryCharge(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    dispensary = models.ForeignKey(Dispensary, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)

class WardCharge(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)
