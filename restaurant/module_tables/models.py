from django.db import models

from accounts.models import Profile


# Create your models here.

class Table(models.Model):
    restaurant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    table_number = models.CharField(max_length=20, blank=True)
    table_type = models.CharField(max_length=50, blank=True)
    capacity = models.CharField(max_length=9, blank=True)
    location = models.CharField(max_length=100, blank=True)
    table_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)
