from django.db import models

from accounts.models import Profile
from module_terms.models import Term
from module_subjects.models import Subject
from module_classes.models import Class
from module_students.models import Student


# Create your models here.

class Assessment(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    clas = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    assessment_code = models.CharField(max_length=20, blank=True)
    assessment_name = models.CharField(max_length=100, blank=True)
    assessment_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class AssessmentSheet(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.CharField(max_length=10, blank=True)
    grade = models.CharField(max_length=10, blank=True)
    remarks = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.id)

