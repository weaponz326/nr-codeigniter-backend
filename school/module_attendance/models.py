from django.db import models

from accounts.models import Profile
from module_terms.models import Term
from module_classes.models import Class


# Create your models here.

class Attendance(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # term = models.ForeignKey(Term, on_delete=models.CASCADE)
    source = models.ForeignKey(Class, on_delete=models.CASCADE)
    attendance_code = models.CharField(max_length=20, blank=True)
    attendance_name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.id)
