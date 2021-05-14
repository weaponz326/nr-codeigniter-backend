from django.db import models
# from django.contrib.postgres.fields import ArrayField

from accounts.models import Profile
from module_terms.models import Term


# Create your models here.

class Timetable(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, null=True, on_delete=models.CASCADE)
    timetable_code = models.CharField(max_length=20, blank=True)
    timetable_name = models.CharField(max_length=100, blank=True)
    timetable_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

# class TimetablePeriod(models.Model):
#     timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
#     periods = ArrayField(models.CharField(max_length=20, blank=True), default=list)

#     def __str__(self):
#         return str(self.id)
