from django.db import models

from accounts.models import Profile


# Create your models here.

class Employee(models.Model):
    SEX_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    WORK_STATUS_CHOICES = [('Active', 'Active'), ('Transfered', 'Transfered'), ('Retired', 'Retired')]

    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.FileField(null=True, upload_to='employees')
    nationality = models.CharField(max_length=50, blank=True)
    religion = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    state = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=20, blank=True)
    employee_code = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=100, blank=True)
    pay_grade = models.CharField(max_length=50, blank=True)
    work_status = models.CharField(max_length=50, choices=WORK_STATUS_CHOICES, blank=True)
    started_work = models.DateField(null=True, blank=True)
    ended_work = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
