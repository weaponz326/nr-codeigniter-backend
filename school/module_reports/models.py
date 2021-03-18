from django.db import models

from accounts.models import Profile
from module_terms.models import Term
from module_classes.models import Class


# Create your models here.

class Report(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # term = models.ForeignKey(Term, on_delete=models.CASCADE)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)
    report_code = models.CharField(max_length=20, blank=True)
    report_name = models.CharField(max_length=100, blank=True)
    report_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
