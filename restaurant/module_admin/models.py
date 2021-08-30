from django.db import models
from accounts.models import Profile


# Create your models here.

class User(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    personal_id = models.PositiveIntegerField()
    is_creator = models.BooleanField(default=False)
    user_level = models.CharField(null=True, max_length=20)

    def __str__(self):
        return str(self.personal_id)

class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_access = models.BooleanField(default=False)
    admissions_access = models.BooleanField(default=False)
    appointments_access = models.BooleanField(default=False)
    bills_access = models.BooleanField(default=False)
    diagnosis_access = models.BooleanField(default=False)
    dispensary_access = models.BooleanField(default=False)
    doctors_access = models.BooleanField(default=False)
    drugs_access = models.BooleanField(default=False)
    laboratory_access = models.BooleanField(default=False)
    nurses_access = models.BooleanField(default=False)
    patients_access = models.BooleanField(default=False)
    payments_access = models.BooleanField(default=False)
    portal_access = models.BooleanField(default=False)
    prescriptions_access = models.BooleanField(default=False)
    sittings_access = models.BooleanField(default=False)
    settings_access = models.BooleanField(default=False)
    staff_access = models.BooleanField(default=False)
    wards_access = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Invitation(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    personal_id = models.PositiveIntegerField()
    invitation_status = models.CharField(null=True, max_length=30)
    date_sent = models.DateTimeField(null=True, auto_now=True)
    date_confirmed = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.id)
