from django.db import models

from accounts.models import Profile

# Create your models here.


class ExtendedProfile(models.Model):
    profile = models.ForeignKey(Profile, blank=True, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    phone1 = models.CharField(max_length=20, null=True, blank=True)
    phone2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.id

class Subscription(models.Model):
    profile = models.ForeignKey(Profile, blank=True, on_delete=models.CASCADE)
    subscription = models.CharField(max_length=20, blank=True, default="Individual")
    plan = models.CharField(max_length=20, blank=True, default="Yearly")

    def __str__(self):
        return self.id

