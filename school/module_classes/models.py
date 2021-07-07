from django.db import models

from accounts.models import Profile
from module_terms.models import Term
from module_subjects.models import Subject
from module_teachers.models import Teacher


# Create your models here.

class Class(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, null=True, blank=True)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    class_name = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.id)

class ClassSubject(models.Model):
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
