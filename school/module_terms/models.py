from django.db import models

from accounts.models import Profile


# Create your models here.

class Term(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    term_name = models.CharField(max_length=100, blank=True)
    term_begins = models.DateField(null=True, blank=True)
    term_ends = models.DateField(null=True, blank=True)
    academic_year = models.CharField(max_length=50, blank=True)
    term_status = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)
