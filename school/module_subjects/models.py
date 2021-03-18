from django.db import models

from accounts.models import Profile
from module_terms.models import Term


# Create your models here.

class Subject(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # term = models.ForeignKey(Term, on_delete=models.CASCADE, blank=True, null=True)
    subject_code = models.CharField(max_length=20, blank=True)
    subject_name = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.id)
