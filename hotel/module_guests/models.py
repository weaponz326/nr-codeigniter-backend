from django.db import models

from accounts.models import Profile


# Create your models here.

class Guest(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    guest_code = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    sex = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.id)
