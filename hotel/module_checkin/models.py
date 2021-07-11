from django.db import models

from accounts.models import Profile
from module_bookings.models import Booking
from module_rooms.models import Room


# Create your models here.

class Checkin(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    checkin_code = models.CharField(max_length=20, blank=True)
    checkin_date = models.DateTimeField(null=True, blank=True)
    checkout_date = models.DateTimeField(null=True, blank=True)
    number_nights = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return str(self.id)
