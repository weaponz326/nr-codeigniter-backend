from django.db import models

from accounts.models import Profile
from module_members.models import Member

# Create your models here.

class Attendance(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    attendance_code = models.CharField(max_length=20, blank=True)
    attendance_name = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return str(self.id)

class AttendanceMember(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

class AttendanceDay(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    day = models.DateField(null=True, blank=True)

class AttendanceCheck(models.Model):
    attendance_member = models.ForeignKey(AttendanceMember, on_delete=models.CASCADE)
    day = models.DateField(null=True, blank=True)
    check = models.BooleanField(null=True)
    time_in = models.TimeField(null=True)
