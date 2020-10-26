from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class AdditionalProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.email

class LocationDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.user.email

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    backup_email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.email