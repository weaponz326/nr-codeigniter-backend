from django.db import models
from accounts.models import Profile


# Create your models here.

# field name changed from account to user
# to avoid clashing with model name
class Account(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100, null=True)
    account_number = models.CharField(max_length=50, null=True)
    bank_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(null=True)
    description = models.CharField(max_length=100, null=True)
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)
