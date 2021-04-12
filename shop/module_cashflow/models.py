from django.db import models

from accounts.models import Profile


# Create your models here.

class Sheet(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sheet_code = models.CharField(max_length=20, blank=True)
    sheet_name = models.CharField(max_length=100, blank=True)
    sheet_type = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return str(self.id)