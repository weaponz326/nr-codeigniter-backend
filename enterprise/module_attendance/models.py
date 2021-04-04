from django.db import models

from accounts.models import Profile


# Create your models here.

class Attendance(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    attendance_code = models.CharField(max_length=20, blank=True)
    attendance_name = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return str(self.id)
