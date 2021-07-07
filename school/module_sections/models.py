from django.db import models
# from django.contrib.postgres.fields import ArrayField

from accounts.models import Profile
from module_teachers.models import Teacher
from module_students.models import Student


# Create your models here.

class Section(models.Model):
    
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.id)

class SectionStudent(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
