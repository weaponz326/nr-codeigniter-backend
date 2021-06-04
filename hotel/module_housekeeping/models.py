from django.db import models

from accounts.models import Profile
from module_rooms.models import Room

# Create your models here.

class Housekeeping(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    housekeeping_code = models.CharField(max_length=20, blank=True)
    housekeeping_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class Checklist(models.Model):
    housekeeping = models.ForeignKey(Housekeeping, on_delete=models.CASCADE)
    item_number = models.CharField(max_length=20, blank=True)
    item_description = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.id)
