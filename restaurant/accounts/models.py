from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    logo = models.FileField(null=True, upload_to='profile')

    def __str__(self):
        return str(self.name)
