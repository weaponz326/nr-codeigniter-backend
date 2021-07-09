from django.db import models
from accounts.models import Profile
from module_employees.models import Employee

# Create your models here.

class Payroll(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    payroll_code = models.CharField(max_length=30, null=True)
    payroll_name = models.CharField(max_length=100, null=True)
    payroll_status = models.CharField(max_length=50, null=True)
    date_generated = models.DateField(blank=True, null=True)
    month = models.CharField(max_length=20, null=True)
    year = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.id)

class PayrollSheet(models.Model):
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100, null=True)
    account_number = models.CharField(max_length=30, null=True)
    pay_grade = models.CharField(max_length=30, null=True)
    basic_pay = models.CharField(max_length=15, null=True)
    allowance = models.CharField(max_length=15, null=True)
    tax = models.CharField(max_length=15, null=True)
    salary = models.CharField(max_length=15, null=True)

    def __str__(self):
        return str(self.id)
