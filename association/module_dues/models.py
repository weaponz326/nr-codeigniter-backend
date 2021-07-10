from django.db import models

from accounts.models import Profile
from module_members.models import Member


# Create your models here.

class Dues(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    dues_code = models.CharField(max_length=20, blank=True)
    dues_name = models.CharField(max_length=100, blank=True)
    dues_date = models.DateField(null=True, blank=True)
    amount = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return str(self.id)

class DuesPayment(models.Model):
    dues = models.ForeignKey(Dues, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    payment_date = models.DateField(null=True, blank=True)
    amount = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return str(self.id)
