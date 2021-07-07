from django.db import models

from accounts.models import Profile
from module_terms.models import Term
from module_classes.models import Class
from module_assessment.models import Assessment
from module_students.models import Student


# Create your models here.

class Report(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, null=True, on_delete=models.CASCADE)
    clas = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    report_code = models.CharField(max_length=20, blank=True)
    report_name = models.CharField(max_length=100, blank=True)
    report_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class ReportAssessment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class ReportStudent(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.id)

