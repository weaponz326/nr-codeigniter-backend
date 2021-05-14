from django.db import models

from accounts.models import Profile
from module_classes.models import Class


# Create your models here.

class Student(models.Model):
    SEX_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, blank=True)
    photo = models.FileField(null=True)
    nationality = models.CharField(max_length=50, blank=True)
    religion = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    state = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=20, blank=True)
    student_code = models.CharField(max_length=20, blank=True)
    admission_date = models.DateField(blank=True, null=True)
    previous_school = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)
