from django.db import models

from accounts.models import Profile
from module_guests.models import Guest
from module_rooms.models import Room
from module_services.models import Service

# Create your models here.

class Bill(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    bill_code = models.CharField(max_length=20, blank=True)
    bill_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class RoomBill(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    number_nights = models.CharField(max_length=20, blank=True)
    amount = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)

class ServiceBill(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)
