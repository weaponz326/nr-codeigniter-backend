from django.db import models

from accounts.models import Profile
from module_employees.models import Employee


# Create your models here.

class Attendance(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    attendance_code = models.CharField(max_length=20, blank=True)
    attendance_name = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=10, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class AttendanceSheet(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checks = models.JSONField();

class AttendanceDay(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    day = models.DateField(null=True, blank=True)
