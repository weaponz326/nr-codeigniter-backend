from django.db import models

from accounts.models import Profile


# Create your models here.

class Appraisal(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    appraisal_code = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    supervisor = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)
