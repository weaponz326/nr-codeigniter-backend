from django.db import models

from accounts.models import Profile


# Create your models here.

class Roster(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    roster_code = models.CharField(max_length=20, blank=True)
    roster_name = models.CharField(max_length=100, blank=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)

    def __str__(self):
        return str(self.id)
