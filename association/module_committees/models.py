from django.db import models

from accounts.models import Profile
from module_members.models import Member


# Create your models here.

class Committee(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    committee_name = models.CharField(max_length=200, blank=True)
    date_formed = models.DateField(null=True)
    description = models.TextField(blank=True)
    committee_status = models.CharField(max_length=200, blank=True)
    functions = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.id)

class CommitteeMember(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
