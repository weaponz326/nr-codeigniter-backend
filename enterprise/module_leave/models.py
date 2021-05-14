from django.db import models

from accounts.models import Profile
from module_employees.models import Employee


# Create your models here.

class Leave(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
    leave_code = models.CharField(max_length=20, blank=True)
    date_requested = models.DateField(null=True, blank=True)
    leave_type = models.CharField(max_length=50, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    duration = models.CharField(max_length=20, blank=True)
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return str(self.id)
