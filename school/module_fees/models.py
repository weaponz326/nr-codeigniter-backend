from django.db import models
# from jsonfield import JSONField

from accounts.models import Profile
from module_classes.models import Class
from module_students.models import Student


# Create your models here.

class Fee(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fees_code = models.CharField(max_length=20, blank=True)
    fees_description = models.CharField(max_length=200, blank=True)
    fees_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class TargetClass(models.Model):
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class FeesItem(models.Model):
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, blank=True)
    amount = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return str(self.id)

class ArrearsItem(models.Model):
    fee = models.ForeignKey(Fee, related_name='fee', on_delete=models.CASCADE)
    source = models.ForeignKey(Fee, null=True, related_name='source', on_delete=models.CASCADE)
    item = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.id)

class Bill(models.Model):
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    amount = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return str(self.id)

