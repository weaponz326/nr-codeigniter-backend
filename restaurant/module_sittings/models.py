from django.db import models

from accounts.models import Profile


# Create your models here.

class Sitting(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sitting_code = models.CharField(max_length=20, null=True, blank=True)
    sitting_date = models.DateField(null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    number_guests = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
