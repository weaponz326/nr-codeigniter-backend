from django.db import models

from accounts.models import Profile
from module_members.models import Member


# Create your models here.

class Executive(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, blank=True)
    date_inducted = models.DateField(null=True)
    
    def __str__(self):
        return str(self.id)
