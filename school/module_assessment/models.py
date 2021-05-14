from django.db import models

from accounts.models import Profile
from module_terms.models import Term
from module_subjects.models import Subject


# Create your models here.

class Assessment(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    assessment_code = models.CharField(max_length=20, blank=True)
    assessment_name = models.CharField(max_length=100, blank=True)
    assessment_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
