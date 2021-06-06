from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    task_date = models.DateField(null=True)
    task_time = models.TimeField(null=True)
    task_status = models.BooleanField(null=True)

    def __str__(self):
        return str(self.id)
