from django.db import models

from accounts.models import Profile
from module_members.models import Member


# Create your models here.

class Group(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.id)

class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
