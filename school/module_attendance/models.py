from django.db import models

from accounts.models import Profile
from module_terms.models import Term
from module_classes.models import Class
from module_students.models import Student


# Create your models here.

class Attendance(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, null=True, on_delete=models.CASCADE)
    source = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    attendance_code = models.CharField(max_length=20, blank=True)
    attendance_name = models.CharField(max_length=100, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class AttendanceSheet(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    checks = models.JSONField();

class AttendanceDays(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    days = models.JSONField()
