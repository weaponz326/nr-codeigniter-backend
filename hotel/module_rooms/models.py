from django.db import models

from accounts.models import Profile


# Create your models here.

class Room(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20, blank=True)
    room_type = models.CharField(max_length=50, blank=True)
    location = models.TextField(blank=True)
    rate = models.CharField(max_length=15, blank=True)
    features = models.TextField(blank=True)
    room_status = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)
