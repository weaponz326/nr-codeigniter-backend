from django.db import models

from accounts.models import Profile


# Create your models here.

class Booking(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    booking_code = models.CharField(max_length=20, blank=True)
    booking_date = models.DateField(blank=True)
    guest_name = models.CharField(max_length=100, blank=True)
    expected_arrival = models.DateTimeField(blank=True)
    booking_status = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)
