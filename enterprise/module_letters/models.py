from django.db import models

from accounts.models import Profile


# Create your models here.

class Received(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=50, blank=True)
    letter_date = models.CharField(max_length=20, blank=True)
    sender = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=20, blank=True)
    date_received = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)

class Sent(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=50, blank=True)
    letter_date = models.CharField(max_length=20, blank=True)
    recipient = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=20, blank=True)
    date_sent = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)
