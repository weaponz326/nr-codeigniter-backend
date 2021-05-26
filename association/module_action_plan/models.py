from django.db import models
from accounts.models import Profile


# Create your models here.

class Plan(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=200, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    facilitator = models.CharField(max_length=100, null=True)
    goals = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)

class Step(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    step = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
