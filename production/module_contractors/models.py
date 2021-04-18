from django.db import models

from accounts.models import Profile


# Create your models here.

class Contractor(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    contractor_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=100, blank=True)
    primary_contract = models.CharField(max_length=100, blank=True)
    project_name = models.CharField(max_length=100, blank=True)
    contract_type = models.CharField(max_length=50, blank=True)
    work_description = models.TextField(blank=True)
    contract_status = models.CharField(max_length=50, blank=True)
    work_start_date = models.DateField(null=True, blank=True)
    work_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
