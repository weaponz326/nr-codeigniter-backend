from django.db import models

from accounts.models import Profile


# Create your models here.

class Budget(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    budget_name = models.CharField(max_length=100, null=True)
    budget_type = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Income(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)

class Expenditure(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)