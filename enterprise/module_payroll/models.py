from django.db import models
from accounts.models import Profile


# Create your models here.

class Payroll(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    payroll_name = models.CharField(max_length=100, null=True)
    payroll_status = models.CharField(max_length=50, null=True)
    date_generated = models.DateTimeField(blank=True, null=True)
    month = models.CharField(max_length=20, null=True)
    year = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.id)
