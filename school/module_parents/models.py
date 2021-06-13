from django.db import models

from accounts.models import Profile
from module_students.models import Student


# Create your models here.

class Parent(models.Model):
    SEX_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    parent_code = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, blank=True)
    photo = models.FileField(null=True, upload_to='parents')
    nationality = models.CharField(max_length=50, blank=True)
    religion = models.CharField(max_length=50, blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    state = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)

class ParentWard(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    ward = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
