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

class AttendanceStudent(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class AttendanceDay(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    day = models.DateField(null=True, blank=True)

class AttendanceCheck(models.Model):
    attendance_student = models.ForeignKey(AttendanceStudent, on_delete=models.CASCADE)
    day = models.DateField(null=True, blank=True)
    check = models.BooleanField(null=True)
    time_in = models.TimeField(null=True)
