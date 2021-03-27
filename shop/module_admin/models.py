from django.db import models
from accounts.models import Profile


# Create your models here.

class User(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    personal_id = models.PositiveIntegerField()
    is_creator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return str(self.personal_id)

class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_access = models.BooleanField(default=False)
    cashflow_access = models.BooleanField(default=False)
    customers_access = models.BooleanField(default=False)
    inventory_access = models.BooleanField(default=False)
    invoice_access = models.BooleanField(default=False)
    marketting_access = models.BooleanField(default=False)
    orders_access = models.BooleanField(default=False)
    payments_access = models.BooleanField(default=False)
    payables_access = models.BooleanField(default=False)
    portal_access = models.BooleanField(default=False)
    products_access = models.BooleanField(default=False)
    purcahsing_access = models.BooleanField(default=False)
    receivables_access = models.BooleanField(default=False)
    sales_access = models.BooleanField(default=False)
    settings_access = models.BooleanField(default=False)
    staff_access = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    activity_module = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
