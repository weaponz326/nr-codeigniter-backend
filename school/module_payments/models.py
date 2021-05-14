from django.db import models

from accounts.models import Profile
from module_students.models import Student
from module_fees.models import Fee


# Create your models here.

class Payment(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, null=True, on_delete=models.CASCADE)
    payment_code = models.CharField(max_length=20, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    amount_paid = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return str(self.id)
