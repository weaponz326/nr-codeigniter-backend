from django.db import models
# from jsonfield import JSONField

from accounts.models import Profile


# Create your models here.

class Fee(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fees_code = models.CharField(max_length=20, blank=True)
    fees_description = models.CharField(max_length=200, blank=True)
    fees_date = models.DateField(null=True, blank=True)
    # classes = JSONField()
    # students = JSONField()
    
    def __str__(self):
        return str(self.id)

class FeesItem(models.Model):
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, blank=True)
    amount = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return str(self.id)

