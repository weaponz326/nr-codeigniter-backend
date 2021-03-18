from django.db import models
from accounts.models import Profile

# Create your models here.

class User(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    personal_id = models.PositiveIntegerField()
    is_creator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return str(self.personal_id)

class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_access = models.BooleanField(default=False)
    assessment_access = models.BooleanField(default=False)
    attendance_access = models.BooleanField(default=False)
    classes_access = models.BooleanField(default=False)
    fees_access = models.BooleanField(default=False)
    parents_access = models.BooleanField(default=False)
    payments_access = models.BooleanField(default=False)
    portal_access = models.BooleanField(default=False)
    reports_access = models.BooleanField(default=False)
    settings_access = models.BooleanField(default=False)
    staff_access = models.BooleanField(default=False)
    students_access = models.BooleanField(default=False)
    subjects_access = models.BooleanField(default=False)
    teachers_access = models.BooleanField(default=False)
    terms_access = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    activity_module = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
