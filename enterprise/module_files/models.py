from django.db import models
from accounts.models import Profile


# Create your models here.

class Folder(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=100, null=True)
    folder_number = models.CharField(max_length=50, null=True)
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100, null=True)
    file_number = models.CharField(max_length=50, null=True)
    date_added = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)
