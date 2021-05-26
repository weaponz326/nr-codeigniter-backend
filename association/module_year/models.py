from django.db import models

from accounts.models import Profile


# Create your models here.

class Year(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    year = models.CharField(max_length=100, blank=True)
    year_begins = models.DateField(null=True)
    year_ends = models.DateField(null=True)
    year_status = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return str(self.id)
