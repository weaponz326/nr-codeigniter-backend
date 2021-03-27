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
    accounts_access = models.BooleanField(default=False)
    admin_access = models.BooleanField(default=False)
    appraisal_access = models.BooleanField(default=False)
    aassets_access = models.BooleanField(default=False)
    attendance_access = models.BooleanField(default=False)
    budget_access = models.BooleanField(default=False)
    employees_access = models.BooleanField(default=False)
    files_access = models.BooleanField(default=False)
    leave_access = models.BooleanField(default=False)
    ledger_access = models.BooleanField(default=False)
    letters_access = models.BooleanField(default=False)
    payroll_access = models.BooleanField(default=False)
    portal_access = models.BooleanField(default=False)
    procurement_access = models.BooleanField(default=False)
    reception_access = models.BooleanField(default=False)
    settings_access = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    activity_module = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
