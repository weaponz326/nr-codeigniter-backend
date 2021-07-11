from django.db import models

from accounts.models import Profile
from module_doctors.models import Doctor
from module_nurses.models import Nurse
from module_staff.models import Staff


# Create your models here.

class Roster(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    roster_code = models.CharField(max_length=20, blank=True)
    roster_name = models.CharField(max_length=100, blank=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    source = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)

class Shift(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    shift_name = models.CharField(max_length=100, blank=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return str(self.id)

class Batch(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    batch_name = models.CharField(max_length=100, blank=True)
    batch_symbol = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)

class RosterDay(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    day = models.JSONField()

class RosterSheet(models.Model):
    roster_day = models.ForeignKey(RosterDay, null=True, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, null=True, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.CASCADE)

class DoctorsPersonnel(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class NursesPersonnel(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, null=True, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class StaffPersonnel(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
