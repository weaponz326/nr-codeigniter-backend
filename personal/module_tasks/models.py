from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=300, null=True)
    priority = models.CharField(max_length=50, null=True)
    progress = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.id)
