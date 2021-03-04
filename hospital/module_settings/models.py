from django.db import models

from accounts.models import Profile


# Create your models here.

class ExtendedProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    phone1 = models.CharField(max_length=20, null=True)
    phone2 = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.id
