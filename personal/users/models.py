from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='users_profile', on_delete=models.CASCADE, blank=True)
    location = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.user.email