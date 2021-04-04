from django.db import models

from accounts.models import Profile


# Create your models here.

class Visitor(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    visit_code = models.CharField(max_length=20, blank=True)
    visit_date = models.DateField(null=True, blank=True)
    visitor_name = models.CharField(max_length=100, blank=True)
    visitor_phone = models.CharField(max_length=20, blank=True)
    arrival = models.TimeField(null=True, blank=True)
    departure = models.TimeField(null=True, blank=True)
    purpose = models.CharField(max_length=100, blank=True)
    tag_number = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)
